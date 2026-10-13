import cv2


def start_camera():
    # Open the default webcam.
    # 0 usually means the first camera connected to the computer.
    camera = cv2.VideoCapture(0)

    # Check whether OpenCV was able to access the camera.
    if not camera.isOpened():
        print("Could not open camera.")
        return

    # Load OpenCV's built-in face detection model.
    # This model looks for frontal human faces.
    face_detector = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Keep reading frames from the webcam until the user quits.
    while True:
        # Read one frame from the webcam.
        # success tells us whether the frame was captured correctly.
        success, frame = camera.read()

        if not success:
            print("Could not read camera frame.")
            break

        # Convert the image to grayscale.
        # The face detector does not need full color information.
        gray_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        # Search the frame for faces.
        faces = face_detector.detectMultiScale(
            gray_frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(100, 100)
        )

        # Draw a rectangle around every detected face.
        for x, y, width, height in faces:
            cv2.rectangle(
                frame,
                (x, y),
                (x + width, y + height),
                (0, 255, 0),
                2
            )

        # Name of the OpenCV camera window.
        window_name = "Face Access System - Face Detection"

        # Show the current webcam frame.
        cv2.imshow(window_name, frame)

        # Read the keyboard once for this frame.
        key = cv2.waitKey(1) & 0xFF
        
        # Allow the user to close the program by pressing Q.
        if key == ord("q"):
            break
        # Also stop the loop if the user clicks the X button
        # on the camera window.
        if cv2.getWindowProperty(
            window_name,
            cv2.WND_PROP_VISIBLE
        ) < 1:
            break

    # Release the webcam so other programs can use it.
    camera.release()

    # Close all OpenCV windows.
    cv2.destroyAllWindows()