import cv2
def visage(chemin_image):
    clas=cv2.CascadeClassifier('C:/Users/ASUS/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    if type(chemin_image)==str:
        img=cv2.imread(chemin_image)
    else:
        img=chemin_image
    if len(img.shape)==3:
        grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        grayimg=img
    face=clas.detectMultiScale(grayimg,scaleFactor=1.1,minNeighbors=13)
    if len(face) == 0:
        print(f"Aucun visage detecte dans : {chemin_image}")
        return None

    for x,y,w,h in face:
        vis=img[y:y+h,x:x+w]

    return vis