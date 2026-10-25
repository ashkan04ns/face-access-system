from database import get_face_profiles


def main():
    # Load all enrolled face profiles from PostgreSQL.
    profiles = get_face_profiles()

    if not profiles:
        print("No enrolled face profiles found.")
        return

    for user_id, embedding in profiles:
        print("User ID:", user_id)
        print("Embedding size:", len(embedding))


if __name__ == "__main__":
    main()