# 0. Prerequisites
```shell
# Install pipenv
brew install pipenv
# .zshrc 에 가상환경 환경변수 설정
export PIPENV_IGNORE_VIRTUALENVS=1
export PIPENV_VERBOSITY=-1
```

# 1. Set up the project
```shell
git clone https://github.com/codelab-kr/django-starter.git


# vene init
cd django-starter/apps
pipenv install
pipenv shell

# (Optinal) If the database is not created
# create database
python3 manage.py migrate

# create superuser
python3 manage.py createsuperuser
```


### (Optinal) for development environment
```shell
# install dependencies
yarn set version berry
yard set version stable
yarn install
# watch css
yarn tailwind

# New Terminal
# livereload for django templates
python3 manage.py livereload
```


# 2. Run server
```shell
# New Terminal
python3 manage.py runserver
```


# 3. Access to browser and check
- Server http://localhost:8000
- admin page http://localhost:8000/<hidden>
