import os

import psycopg
from dotenv import load_dotenv


load_dotenv()


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def get_user_permissions(email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        select 
            users.user_id,
            users.name,
            users.email,
            roles.role_name,
            permissions.permission_name
        from users
        join roles on users.role_id = roles.role_id
        join role_permissions on roles.role_id = role_permissions.role_id
        join permissions on role_permissions.permission_id = permissions.permission_id
        where users.email = %s
        order by permissions.permission_id;
        """,
        (email,)
    )

    results = cursor.fetchall()

    cursor = cursor.close()
    connection.close()

    return results

def save_face_embedding(user_id, embedding):
    #Connect to PostgreSQL database
    connection = get_connection()
    cursor = connection.cursor()

    #Save the face embedding to the user.

    #user_id is unique in face_profiles, so if this user already has an enroll face, update it instead of creating a duplicate.

    cursor.execute(
        """
        INSERT INTO face_profiles(
        user_id,
        face_embedding
        )
        VALUES (%s, %s)
        ON CONFLICT (user_id) DO UPDATE SET face_embedding = EXCLUDED.face_embedding, created_at = CURRENT_TIMESTAMP;
        """,
        (user_id, embedding)
    )

    #Insert/Update operation is need to be committed.
    connection.commit()

    cursor.close()
    connection.close()

def get_face_profiles():
    # Connect to PostgreSQL.
    connection = get_connection()
    cursor = connection.cursor()

    # Retrieve every enrolled user's stored face embedding.
    cursor.execute(
        """
        SELECT
            face_profiles.user_id,
            face_profiles.face_embedding
        FROM face_profiles;
        """
    )

    profiles = cursor.fetchall()

    cursor.close()
    connection.close()

    return profiles