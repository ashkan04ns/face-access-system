# Face Access System

A Python, PostgreSQL, and computer-vision project for building a facial verification and role-based access control system.

The system is designed to enroll consenting users, generate numerical face embeddings from their images, store those embeddings in PostgreSQL, and eventually verify users through a live webcam before retrieving their roles and permissions.

## Current Features

- PostgreSQL relational database
- User and role management
- Role-based access control (RBAC)
- Permission mapping
- Python-to-PostgreSQL integration using psycopg
- Parameterized SQL queries
- Environment-based database configuration
- Admin, Manager, and Employee test roles
- Webcam face detection using OpenCV
- Face detection using the pretrained YuNet model
- Face embedding generation using the pretrained SFace model
- Multi-image face enrollment
- Face embedding normalization and averaging
- Storage of 128-value face embeddings in PostgreSQL
- Retrieval of stored face profiles from Python

## Face Enrollment Pipeline

The current enrollment process works as follows:

```text
Enrollment Photos
        ↓
YuNet Face Detection
        ↓
Face Alignment
        ↓
SFace Feature Extraction
        ↓
128-Value Face Embedding
        ↓
Average Multiple Embeddings
        ↓
Normalize Final Embedding
        ↓
PostgreSQL face_profiles Table
```

Multiple enrollment photos can be used for a single user. The generated embeddings are averaged and normalized before one final embedding is stored in the database.

## Database Structure

The current database contains:

- `users` - registered application users
- `roles` - available user roles
- `permissions` - available application permissions
- `role_permissions` - maps roles to permissions
- `face_profiles` - stores enrolled users' face embeddings
- `access_logs` - prepared for authentication attempt history

## Roles and Permissions

### Admin

- `VIEW_DASHBOARD`
- `VIEW_REPORTS`
- `MANAGE_USERS`
- `VIEW_ACCESS_LOGS`

### Manager

- `VIEW_DASHBOARD`
- `VIEW_REPORTS`

### Employee

- `VIEW_DASHBOARD`

## Technologies

- Python
- PostgreSQL
- SQL
- OpenCV
- YuNet face detection
- SFace face recognition
- NumPy
- psycopg
- python-dotenv
- Git / GitHub

## Project Structure

```text
face-access-system/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── face_service.py
│   ├── enrollment.py
│   └── recognition.py
│
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   └── queries/
│       ├── user_roles.sql
│       └── role_permissions.sql
│
├── data/
│   └── enrollment/
│       └── user_1/
│
├── models/
│   ├── face_detection_yunet_2023mar.onnx
│   └── face_recognition_sface_2021dec.onnx
│
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

The local enrollment images and downloaded ONNX model files are excluded from Git and are not committed to the repository.

## Current Development Status

Completed:

- PostgreSQL database design
- User, role, and permission system
- Role-based access control
- Python database integration
- Webcam access
- Basic webcam face detection
- YuNet and SFace model integration
- Photo-based face enrollment
- Multi-image embedding generation
- Face embedding storage and retrieval

## Planned Features

- Live webcam facial verification
- Matching live face embeddings against enrolled users
- Unknown-user rejection
- Retrieval of recognized users' roles and permissions
- Authentication attempt logging
- Role-based dashboard interface
- Basic liveness / spoofing protection
- Recognition performance evaluation under different lighting, angles, and distances
- Automated testing
- User interface

## Security and Privacy

Database credentials are stored locally in a `.env` file and are excluded from Git using `.gitignore`.

Enrollment photos are treated as local biometric data and are excluded from the repository.

Downloaded face-model files are also excluded from Git and must be obtained separately.

This project is a prototype for learning computer vision, databases, and role-based access control.