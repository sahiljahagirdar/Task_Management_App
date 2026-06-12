# Task Management App

A Task Management Application built using **FastAPI** that allows users to create, manage, and track tasks efficiently.

## Features

### Authentication

* User registration and login.
* Secure authentication using JWT (JSON Web Tokens).
* Password hashing for enhanced security.

### Authorization

* Role-based access control (RBAC).
* Different permissions based on user roles.
* Protected API endpoints.

### Task Management

* Create tasks.
* Update task details.
* Delete tasks.
* View assigned and created tasks.
* Track task completion status.

### Role-Based Task Assignment

* Admins can assign tasks to users.
* Users can view and manage tasks assigned to them.
* Access restrictions based on assigned roles.

## Technology Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Authentication:** JWT
* **Data Validation:** Pydantic

## Project Structure

```text
task_management_app/
│
├── src/
│   ├── auth/
│   ├── users/
│   ├── tasks/
│   ├── database/
│   └── utils/
│
├── main.py
├── requirements.txt
└── README.md
```

## API Modules

* Authentication Module
* User Management Module
* Task Management Module
* Role & Permission Management Module

## Future Enhancements

* Task priority management
* Due dates and reminders
* Email notifications
* Activity logs
* Team collaboration features
* Dashboard and analytics
* File attachments for tasks
* Docker deployment
* CI/CD integration

## Status

🚧 Project currently under development. More features and documentation will be added as the project progresses.
