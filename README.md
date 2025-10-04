# Task Management API

This project is a **Task Management System** built with **Django Rest Framework (DRF)**.  
It provides user authentication with JWT and allows users to create and manage categories, boards, and tasks.  
The project also includes API documentation, logging, rate limiting, and testing.

## Features

- **User Authentication**
  - User registration, login, and logout using JWT authentication.

- **Task Management**
  - Create, retrieve, update, and delete categories.
  - Create, retrieve, update, and delete boards.
  - Create, retrieve, update, and delete tasks.

- **Security and Rate Limiting**
  - Configured **DRF Throttling** to handle request rate limiting.

- **Logging**
  - Uses Django’s built-in logging system to track application activity.

- **API Documentation**
  - Integrated with **drf-spectacular** for OpenAPI/Swagger documentation.

- **Testing**
  - Includes unit tests using Django’s built-in test framework.

## Technologies Used

- **Backend**: Django, Django Rest Framework (DRF)
- **Authentication**: JWT (JSON Web Token)
- **Database**: MySQL
- **Containerization**: Docker
- **Web Server**: Nginx
- **Documentation**: drf-spectacular
- **Language**: Python

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task_management.git
   cd TaskManagement
   ```

2. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Apply migrations:
   ```bash
   docker exec -it task_management python manage.py migrate
   ```

4. Create a superuser (optional):
   ```bash
   docker exec -it task_management python manage.py createsuperuser
   ```

## API Documentation

Once the server is running, the API documentation is available at:

```
http://localhost:8000/api/schema/swagger-ui/
```

or

```
http://localhost:8000/api/schema/redoc/
```

## License

This project is licensed under the MIT License.
