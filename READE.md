# Django Task Management Project

This is a simple Django project with user authentication and task management functionality. Users can register, log in, view their tasks, and mark them as completed.

## Features

- User Registration
- User Login/Logout
- Task Management
  - Create Tasks
  - View Own Tasks
  - Mark Tasks as Completed

## Requirements

- Python 3.8+
- Django 3.2+
- SQLite (default, but can be changed to other databases)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mujahid141/tms.git
   cd django-task-management


Create a virtual environment and activate it:


python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the required packages:

pip install -r requirements.txt
Apply the migrations:

python manage.py migrate
Create a superuser:
python manage.py createsuperuser
Run the development server:

python manage.py runserver
