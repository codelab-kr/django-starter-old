# Generated by Django 5.0.4 on 2024-05-06 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("acts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="act",
            name="url",
        ),
    ]
