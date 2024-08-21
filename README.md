## Task Management System API (Level 2)

This project implements an advanced Task Management System API using Django and Django REST Framework. It extends the basic functionalities of a task management system by introducing user authentication, project management, task assignments, comments, and advanced business logic.


### Features

* User Authentication (Django REST Framework Simple JWT)
* Project Management
    * Create, retrieve, update, and delete projects.
* Task Management
    * Create, retrieve, update, and delete tasks.
    * Assign tasks to users.
    * Mark tasks as completed.
    * Calculate overdue tasks.
* Comments
    * Add comments to tasks.
* Project Progress Calculation
    * Calculate the progress of a project based on the status of its tasks.


### Technologies Used

* Python
* Django
* Django REST Framework
* djangorestframework-simplejwt (for authentication)


### Project Structure

```
task_api/
├── manage.py
├── task/
│   ├── asgi.py
│   ├── wsgi.py
│   ├── url.py
│   ├── settings.py
├── TaskAPI/
│   ├── admin.py
│   ├── apps.py
│   ├── factories.py  # New! Factories for object creation
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py  # (Optional) Unit tests
│   └── views.py

```


### Installation

1. Clone this repository.
2. Create a virtual environment and activate it.
3. use docker yml file for setup or deployment or Install required dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create a Django secret key:

```bash
python manage.py generate_secret_key --base64
```

6. Update the `SECRET_KEY` in your `settings.py` file with the generated key.
7. (Optional) Create a superuser for initial login:

```bash
python manage.py createsuperuser
```


### Running the API

1. Start the development server:

```bash
python manage.py runserver
```

2. The API will be accessible at http://localhost:8000/


### Usage

**Authentication:**

1. Obtain an authentication token by making a POST request to `/api/token/` with your username and password.
2. Include the obtained token in the `Authorization` header of subsequent API requests:

```
Authorization: Bearer <your_token>
```

**API Endpoints:**

**Users:** (Authentication required for all user endpoints)

* `/api/users/`: Retrieve a list of users (GET) - Requires admin permissions

**Projects:**

* `/api/projects/`:
    * Retrieve a list of projects (GET)
    * Create a new project (POST)
* `/api/projects/<id>/`:
    * Retrieve details of a specific project (GET)
    * Update an existing project (PUT)
    * Delete a project (DELETE)
* `/api/projects/<id>/progress/`: Calculate the progress of a specific project (GET)

**Tasks:**

* `/api/tasks/`:
    * Retrieve a list of tasks (GET)
    * Create a new task (POST)
* `/api/tasks/<id>/`:
    * Retrieve details of a specific task (GET)
    * Update an existing task (PUT)
    * Delete a task (DELETE)
    * Mark a task as completed (POST to `/complete/`)
* `/api/tasks/overdue/`: Retrieve a list of overdue tasks (GET)

**Task Assignments:**

* `/api/tasks/<task_id>/assign/`: Assign a task to a user (POST)
* `/api/tasks/<task_id>/unassign/`: Unassign a task from a user (POST)

**Comments:**

* `/api/tasks/<task_id>/comments/`:
    * Retrieve all comments on a task (GET)
    * Add a comment to a task (POST)
* `/api/tasks/<task_id>/comments/<comment_id>/`: Delete a specific comment (DELETE)


### Documentation

This README provides a basic overview of the API. Additional documentation and examples can be found in the code comments and within the Django REST Framework browsable API documentation (accessible at http://localhost:8000/api/ after running the server).


