from django.test import TestCase

from .forms import TaskForm
from .models import Task


class TaskModelTest(TestCase):
    def test_task_model_exists(self):
        tasks = Task.objects.count()
        self.assertEqual(tasks, 0)

    def test_task_model_has_string_representation(self):
        task = Task.objects.create(title="Test task")
        self.assertEqual(str(task), "Test task")


class IndexTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Test task")

    def test_index_page_returns_correct_response(self):
        response = self.client.get("/tasks/")
        self.assertTemplateUsed(response, "tasks/tasks.html")
        self.assertEqual(response.status_code, 200)

    def test_index_page_has_tasks(self):
        response = self.client.get("/tasks/")
        self.assertContains(response, self.task.title)


class AddTest(TestCase):
    def setUp(self):
        self.form = TaskForm

    def test_form_is_valid(self):
        self.assertTrue(issubclass(self.form, TaskForm))
        self.assertTrue("title" in self.form().fields)
        self.assertTrue("description" in self.form().fields)

        form = self.form(data={"title": "Add task", "description": "Add description"})
        self.assertTrue(form.is_valid())

    def test_add_page_form_renders(self):

        # Test invalid form data
        response = self.client.post(
            "/tasks/add/",
            {"title": "", "description": "Add description"},
        )
        self.assertContains(response, "This field is required.")

        # Test valid form data
        response = self.client.post(
            "/tasks/add/",
            {"title": "Add task", "description": "Add description"},
        )
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.first()
        self.assertEqual(task.title, "Add task")
        self.assertEqual(task.description, "Add description")


class EditTest(TestCase):
    def setUp(self):
        self.form = TaskForm
        self.task = Task.objects.create(
            title="Test task", description="Test description"
        )
        self.task2 = Task.objects.create(
            title="Another task", description="Another description"
        )

    def test_edit_page_returns_correct_response(self):
        response = self.client.get(f"/tasks/{self.task.id}/edit/")
        self.assertTemplateUsed(response, "tasks/partials/edit.html")
        self.assertEqual(response.status_code, 200)

    def test_form_is_valid(self):
        self.assertTrue(issubclass(self.form, TaskForm))
        self.assertTrue("title" in self.form().fields)
        self.assertTrue("description" in self.form().fields)

        form = self.form(
            data={"title": "Add task", "description": "Add description"},
            instance=self.task,
        )
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(self.task.title, "Add task")

    def test_from_is_invalid(self):
        form = self.form(
            data={"title": "", "description": "Add description"},
            instance=self.task,
        )
        self.assertFalse(form.is_valid())

    def test_edit_page_has_correct_content(self):
        response = self.client.get(f"/tasks/{self.task.id}/edit/")
        self.assertContains(response, self.task.title)
        self.assertContains(response, self.task.description)

    def test_edit_page_does_not_have_incorrect_content(self):
        response = self.client.get(f"/tasks/{self.task.id}/edit/")
        self.assertNotContains(response, self.task2.title)
        self.assertNotContains(response, self.task2.description)

    def test_edit_page_form_renders(self):
        response = self.client.get(f"/tasks/{self.task.id}/edit/")
        self.assertContains(response, "<form")
        self.assertContains(response, "csrfmiddlewaretoken")

        # Test invalid form data
        response = self.client.post(
            f"/tasks/{self.task.id}/edit/",
            {"id": self.task.id, "title": "", "description": "Add description"},
            instance=self.task,
        )
        self.assertContains(response, "This field is required.")

        # Test valid form data
        response = self.client.post(
            f"/tasks/{self.task.id}/edit/",
            {
                "id": self.task.id,
                "title": "updated task",
                "description": "updated description",
            },
            instance=self.task,
        )
        # print(Task.objects.all())
        self.assertEqual(Task.objects.count(), 2)
        task = Task.objects.first()
        self.assertEqual(task.title, "updated task")
        self.assertEqual(task.description, "updated description")


class DeletePageTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Test task")

    def test_delete_page_returns_correct_response(self):
        self.assertEqual(Task.objects.count(), 1)
        self.client.delete(f"/tasks/{self.task.id}/delete/")
        self.assertEqual(Task.objects.count(), 0)
