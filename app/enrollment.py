from pathlib import Path
import cv2
import numpy as np

from database import save_face_embedding



#find the project root regardless of where this script is being run from
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Path to the pretrained YuNet face detector model.
DETECTOR_MODEL = (
    PROJECT_ROOT
    / "models"
    / "face_detection_yunet_2023mar.onnx"
)

# Path to the pretrained SFace recognition model.
RECOGNIZER_MODEL = (
    PROJECT_ROOT
    / "models"
    / "face_recognition_sface_2021dec.onnx"
)

# Folder containing enrollment photos for user_id = 1.
ENROLLMENT_FOLDER = (
    PROJECT_ROOT
    / "data"
    / "enrollment"
    / "user_1"
)

USER_ID = 1

def normalize_embedding(embedding): 
    #calculate the length of embedding vector.

    magnitude = np.linalg.norm(embedding)

    #prevent division by zero
    if magnitude == 0:
        return embedding

    #scale the vector so its total length becomes 1.
    return embedding / magnitude

def create_face_models():
    #Load YuNet, which detects faces and facial landmarks.
    detector = cv2.FaceDetectorYN.create(
        str(DETECTOR_MODEL),
        "",
        (320, 320),
        0.6,
        0.3,
        5000
)
    #Load SFace, which creates the numerical face embeddings.
    recognizer = cv2.FaceRecognizerSF.create(
        str(RECOGNIZER_MODEL),
        ""
    )
    return detector, recognizer
def resize_image(image, max_dimension=1280):
    # Get the original image dimensions.
    height, width = image.shape[:2]

    # If the image is already small enough,
    # no resizing is necessary.
    if max(height, width) <= max_dimension:
        return image

    # Calculate a scale that keeps the original aspect ratio.
    scale = max_dimension / max(height, width)

    new_width = int(width * scale)
    new_height = int(height * scale)

    # Resize the image while preserving its proportions.
    resized_image = cv2.resize(
        image,
        (new_width, new_height),
        interpolation=cv2.INTER_AREA
    )

    return resized_image

def create_embedding(image, detector, recognizer):
    # Resize large phone photos before face detection.
    image = resize_image(image)
    #YuNet needs to know the size of the image being processed.
    height, width = image.shape[:2]

    detector.setInputSize((width, height))

    #Detect the faces in the image.
    _, faces = detector.detect(image)

    #Enrollment images, should contain exactly one detectable face.

    if faces is None:
        return None, "No face detected."

    if len(faces) != 1:
        return None, "More than one face detected."

    face = faces[0]

    #Align and Crop the face using the facial landmarks founded by YuNet.
    aligned_face = recognizer.alignCrop(image, face)

    #generate the numerical representation of the face.

    embedding = recognizer.feature(aligned_face)

    #Normalize before combining multiple enrollment photos.
    embedding = normalize_embedding(embedding)

    return embedding, None

def enroll_user():
    detector, recognizer = create_face_models()

    #Allow JPG, JPEG and PNG enrollment images.

    image_files = sorted(
        [
            path
            for path in ENROLLMENT_FOLDER.iterdir()
            if path.suffix.lower()
            in {".jpg", ".jpeg", ".png"}
        ]
    )

    if not image_files:
        print("No enrollment images found.")
        return

    embeddings = []

    for image_path in image_files:
        print(f"Processing: {image_path.name}")

        #load the image from disk.
        image = cv2.imread(str(image_path))
        
        if image is None:
            print(" Skipped: Could not load image.")
            continue

        embedding, error = create_embedding(image, detector, recognizer)

        if error:
            print(f" Skipped: {error}.")
            continue
        
        embeddings.append(embedding)

        print( "Face embedding created.")

        if not embeddings:
            print("Enrollment failed: No usable face found.")
            return

    #combine all valid enrollment photos into one representative embedding.

    average_embedding = np.mean(embeddings, axis=0)

    average_embedding = normalize_embedding(average_embedding)

    #PostgreSQL DOUBLE PERCISION[] expects ordinary Python numbers rather than a NumPy array.

    embedding_list = np.asarray(
        average_embedding,
        dtype=np.float64).reshape(-1).tolist()

    save_face_embedding(USER_ID, embedding_list)

    print()
    print("Enrollment successful")
    print("USER ID:", USER_ID)
    print("photo used:", len(embeddings))


if __name__ == "__main__":
    enroll_user()