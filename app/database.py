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