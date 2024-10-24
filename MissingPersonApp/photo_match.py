import cv2

def is_face_match(image1_path, image2_path):
    # Load the images using OpenCV
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Check if images are loaded properly
    if image1 is None or image2 is None:
        print("Error: One of the images could not be loaded.")
        return False

    # Convert the images to grayscale
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Load OpenCV's pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in both images
    faces_image1 = face_cascade.detectMultiScale(gray_image1, 1.3, 5)
    faces_image2 = face_cascade.detectMultiScale(gray_image2, 1.3, 5)

    # If no face is detected in any of the images, return False
    if len(faces_image1) == 0 or len(faces_image2) == 0:
        print("No face detected in one or both images.")
        return False

    # Crop and resize the faces from both images for comparison
    (x1, y1, w1, h1) = faces_image1[0]
    face1 = cv2.resize(gray_image1[y1:y1+h1, x1:x1+w1], (200, 200))

    (x2, y2, w2, h2) = faces_image2[0]
    face2 = cv2.resize(gray_image2[y2:y2+h2, x2:x2+w2], (200, 200))

    # Calculate the difference between the two face images
    difference = cv2.absdiff(face1, face2)
    score = cv2.norm(difference, cv2.NORM_L2)

 
    print(f"Face match score: {score}")

    # Set a threshold to consider it a match (you can tune this value)
    if score < 5000:  
        print("Faces match.")
        return True
    
    print("Faces do not match.")
    return False
