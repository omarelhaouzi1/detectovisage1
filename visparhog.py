import dlib
import cv2

def hogvisage(chemin_image):
    detector = dlib.get_frontal_face_detector()

    if isinstance(chemin_image, str):
        img = cv2.imread(chemin_image)
        if img is None:
            print(f"Impossible de lire l'image : {chemin_image}")
            return None
    else:
        img = chemin_image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    if len(faces) == 0:
        print(f"Aucun visage détecté dans : {chemin_image}")
        return None

   
    face = faces[0]
    x, y, w, h = face.left(), face.top(), face.width(), face.height()

  
    x = max(0, x)
    y = max(0, y)
    w = min(w, img.shape[1] - x)
    h = min(h, img.shape[0] - y)

    visage_img = img[y:y+h, x:x+w]

    return visage_img