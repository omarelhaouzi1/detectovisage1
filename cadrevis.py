import cv2
from vecteur import *
from comp import *
from remplircsv import *
import numpy,os
from Presence import *
def visagecam():
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor1.csv")
    clas=cv2.CascadeClassifier('C:/Users/ASUS/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    vid=cv2.VideoCapture(0)
    # listvisage=[]
    while True:
        
        res, cam=vid.read()
        cam=cv2.flip(cam,1)
        grayimg=cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
        face=clas.detectMultiScale(grayimg,scaleFactor=1.1,minNeighbors=13)
        for i,(x,y,w,h)in enumerate(face):
            vis=cam[y:y+h,x:x+w]
            # vis = cv2.resize(vis, (128, 128))
            vect=vecteur(vis)
            indice=compareVect(vect)
            if indice != -1:
                res=presence(indice)
                if res==1:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "Cette personne existait deje il y a deux heures ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
                else:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "cette personne est ajoutee au fichier csv ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
            else:
                cv2.rectangle(cam,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(cam, "cette Personne est inconnu", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
        cv2.imshow("cam",cam)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
    
def visagecamhog():
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor_hog.csv")
    clas=cv2.CascadeClassifier('C:/Users/ASUS/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    vid=cv2.VideoCapture(0)
    # listvisage=[]
    while True:
        
        res, cam=vid.read()
        cam=cv2.flip(cam,1)
        grayimg=cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
        face=clas.detectMultiScale(grayimg,scaleFactor=1.1,minNeighbors=13)
        for i,(x,y,w,h)in enumerate(face):
            vis=cam[y:y+h,x:x+w]
            # vis = cv2.resize(vis, (128, 128))
            vect=extract_hog_vector(vis)
            indice=comparehogVect(vect)
            if indice != -1:
                reslt=hogpresence(indice)
                if reslt==1:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "Cette personne existait deje il y a deux heures ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
                else:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "cette personne est ajoutée au fichier csv ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
            else:
                cv2.rectangle(cam,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(cam, "cette Personne est inconnu", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
        cv2.imshow("cam",cam)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
    
def visagecamlbp():
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor_lbp.csv")
    clas=cv2.CascadeClassifier('C:/Users/ASUS/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    vid=cv2.VideoCapture(0)
    # listvisage=[]
    while True:
        
        res, cam=vid.read()
        cam=cv2.flip(cam,1)
        grayimg=cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
        face=clas.detectMultiScale(grayimg,scaleFactor=1.1,minNeighbors=13)
        for i,(x,y,w,h)in enumerate(face):
            vis=cam[y:y+h,x:x+w]
            # vis = cv2.resize(vis, (128, 128))
            vect=vecteur_lbp_complet(vis)
            indice=comparelbpVect(vect)
            if indice != -1:
                res=lbppresence(indice)
                if res==1:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "Cette personne existait deje il y a deux heures ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
                else:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "cette personne est ajoutée au fichier csv ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
            else:
                cv2.rectangle(cam,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(cam, "cette Personne est inconnu", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
        cv2.imshow("cam",cam)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
    
def visagecamhsv():
    clas=cv2.CascadeClassifier('C:/Users/ASUS/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    vid=cv2.VideoCapture(0)
    while True:
        res, cam=vid.read()
        grayimg=cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
        face=clas.detectMultiScale(grayimg,scaleFactor=1.1,minNeighbors=13)
        for i,(x,y,w,h)in enumerate(face):
            vis=cam[y:y+h,x:x+w]
            # vis = cv2.resize(vis, (128, 128))
            vect=hsv(vis)
            indice=compareVect_cosine(vect)
            if indice != -1:
                res=hsvpresence(indice)
                if res==1:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "Cette personne existait deje il y a deux heures ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
                else:
                    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(cam, "cette personne est ajoutée au fichier csv ", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)
            else:
                cv2.rectangle(cam,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(cam, "cette Personne est inconnu", (x, y+h),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
        cv2.imshow("cam",cam)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
    
