# Face Access System

A Python and PostgreSQL project for building a facial verification and role-based access control system.

The system is being developed to identify enrolled users, retrieve their roles and permissions from a PostgreSQL database, and provide access to application features based on those permissions.

## Current Features

- PostgreSQL relational database
- User and role management
- Role-based access control (RBAC)
- Permission mapping
- Python-to-PostgreSQL integration
- Parameterized SQL queries
- Environment-based database configuration
- Test users for Admin, Manager, and Employee roles

## Database Structure

The current database contains:

- `users` - registered application users
- `roles` - available user roles
- `permissions` - available application permissions
- `role_permissions` - maps roles to permissions
- `face_profiles` - prepared for storing enrolled face embeddings
- `access_logs` - prepared for authentication attempt history

## Roles and Permissions

### Admin
- VIEW_DASHBOARD
- VIEW_REPORTS
- MANAGE_USERS
- VIEW_ACCESS_LOGS

### Manager
- VIEW_DASHBOARD
- VIEW_REPORTS

### Employee
- VIEW_DASHBOARD

## Technologies

- Python
- PostgreSQL
- SQL
- psycopg
- python-dotenv

## Project Structure

```text
face-access-system/
│
├── app/
│   ├── main.py
│   └── database.py
│
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   └── queries/
│       ├── user_roles.sql
│       └── role_permissions.sql
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Planned Features

- Webcam face detection
- Face enrollment
- Facial verification using face embeddings
- Role-based dashboard
- Authentication logging
- Recognition performance evaluation
- User interface

## Security

Database credentials are stored in a local `.env` file and are excluded from Git using `.gitignore`.

This project is intended as an educational prototype and not as a replacement for production-grade authentication systems.