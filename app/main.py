from database import get_user_permissions


def main():
    email = "employee@example.com"

    results = get_user_permissions(email)

    if not results:
        print("User not found.")
        return

    user_id = results[0][0]
    name = results[0][1]
    email = results[0][2]
    role = results[0][3]

    permissions = []

    for row in results:
        permissions.append(row[4])

    print("User ID:", user_id)
    print("Name:", name)
    print("Email:", email)
    print("Role:", role)

    print("\nPermissions:")

    for permission in permissions:
        print("-", permission)


if __name__ == "__main__":
    main()