import cv2
import dlib
import cv2
from lbpmoment import *
from hogcomp import *
from hogvect import *
from remplircsv import *
import numpy,os
from Presence import *
def glob_hog_cam():
    dect=dlib.get_frontal_face_detector()
    vid=cv2.VideoCapture(0) 
    while True:
        resp,cam=vid.read()
        cam=cv2.flip(cam,1)
        faces=dect(cam,2)
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            vis=cam[y:y+h,x:x+w]
            vect=vecteur(vis)
            indice=compareVect(vect)
            if indice != -1:
                res=presence(indice)
                if res==1:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "cette personne deja existe 2 heurs avant ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
                else:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "cette personne est ajoutée au fichier csv ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
            else:
                cv2.rectangle(cam,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(cam, "cette Personne est inconnu", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow("cam",cam)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
def hsv_hog_cam():
    dect=dlib.get_frontal_face_detector()
    vid=cv2.VideoCapture(0) 
    while True:
        resp,cam=vid.read()
        faces=dect(cam,2)
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            vis=cam[y:y+h,x:x+w]
            vect=hsv(vis)
            indice=comparehsvVect(vect)
            if indice != -1:
                res=hsvpresence(indice)
                if res==1:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "ce personne deja existe 2 heurs avant ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
                else:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "cette personne est ajoutée au fichier csv ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
            else:
                cv2.rectangle(cam,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(cam, "ce Personne est inconnu", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow("cam",cam)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
def hog_hog_cam():
    dect=dlib.get_frontal_face_detector()
    vid=cv2.VideoCapture(0) 
    while True:
        resp,cam=vid.read()
        faces=dect(cam,2)
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            vis=cam[y:y+h,x:x+w]
            vect=extract_hog_vector(vis)
            indice=comparehogVect(vect)
            if indice != -1:
                res=hogpresence(indice)
                if res==1:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "ce personne deja existe 2 heurs avant ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
                else:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "cette personne est ajoutée au fichier csv ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
            else:
                cv2.rectangle(cam,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(cam, "ce Personne est inconnu", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow("cam",cam)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
def lbp_hog_cam():
    dect=dlib.get_frontal_face_detector()
    vid=cv2.VideoCapture(0) 
    while True:
        resp,cam=vid.read()
        faces=dect(cam,2)
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            vis=cam[y:y+h,x:x+w]
            vect=vecteur_lbp_complet(vis)
            indice=comparelbpVect(vect)
            if indice != -1:
                res=lbppresence(indice)
                if res==1:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "ce personne deja existe 2 heurs avant ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
                else:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "cette personne est ajoutée au fichier csv ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
            else:
                cv2.rectangle(cam,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(cam, "ce Personne est inconnu", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow("cam",cam)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break