from face_service import start_camera


def main():
    # Start the webcam and face-detection system.
    start_camera()


# Run main() only when this file is executed directly.
if __name__ == "__main__":
    main()