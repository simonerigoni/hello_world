# Django Hello World Project

## Introduction

A simple Django application that displays "Hello World!".

## Software and libraries

This project uses Python 3.11.9 and the most important packages are:

- [django](https://www.djangoproject.com/)

To create the virtual enviroment you can run `python -m venv .venv`.

To install django you can run `pip install django`.

## Running the code

First apply migrations:

`python manage.py makemigrations`

`python manage.py migrate`

Then you can run the server with `python manage.py runserver`. Now you can open your web browser and visit http://127.0.0.1:8000/.
