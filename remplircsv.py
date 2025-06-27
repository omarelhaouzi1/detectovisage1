import cv2
import pandas as pd
import numpy as np
import os
from hogvect import *
import mysql.connector
from haarvect import *
from visparharcascade import *
from visparharcascade import *
def remplissagecsvfichier(id,chemin_dossier):
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor1.csv")
    for i, img_name in enumerate(os.listdir(chemin_dossier)):
        chemin=os.path.join(chemin_dossier,img_name)
        if os.path.isfile(chemin):
            clas=cv2.CascadeClassifier('C:/Users/ASUS/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml')
            vis=visage(chemin)
            v1=vecteur(vis)
            vectstr = " ".join(map(str, v1))
            nwid=(id*10)+i
            if nwid in df['indice'].values:
                print("cet id deja existe")
                print(nwid)
                return 0
            else:
           
                df.loc[len(df)]={'indice': nwid, 'vecteur': vectstr}
                df.to_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor1.csv", index=False)
def remplissagehogcsvfichier(id,chemin_dossier):
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor_hog.csv")
    for i, img_name in enumerate(os.listdir(chemin_dossier)):
        chemin=os.path.join(chemin_dossier,img_name)
        if os.path.isfile(chemin):
            vis=visage(chemin)
            v1=extract_hog_vector(vis)
            vectstr = " ".join(map(str, v1))
            nwid=(id*10)+i
        if nwid in df['indice'].values:
            print("cet id deja existe")
            print(nwid)
            return 0
        else:
           
            df.loc[len(df)]={'indice': nwid, 'vecteur': vectstr}
            df.to_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor_hog.csv", index=False)
def remplissagelbpcsvfichier(id,chemin_dossier):
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor_lbp.csv")
    for i, img_name in enumerate(os.listdir(chemin_dossier)):
        chemin=os.path.join(chemin_dossier,img_name)
        if os.path.isfile(chemin):
            vis=visage(chemin)
            v1=vecteur_lbp_complet(vis)
            vectstr = " ".join(map(str, v1))
            nwid=(id*10)+i
        if nwid in df['indice'].values:
            print("cet id deja existe")
            print(nwid)
            return 0
        else:
           
            df.loc[len(df)]={'indice': nwid, 'vecteur': vectstr}
            df.to_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor_lbp.csv", index=False)
 
def remplissagehsvcsvfichier(id,chemin_dossier):
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor_hsv.csv")
    for i, img_name in enumerate(os.listdir(chemin_dossier)):
        chemin=os.path.join(chemin_dossier,img_name)
        if os.path.isfile(chemin):
            vis=visage(chemin)
            v1=hsv(vis)
            vectstr = " ".join(map(str, v1))
            nwid=(id*10)+i
        if nwid in df['indice'].values:
            print("cet id deja existe")
            print(nwid)
            return 0
        else:
           
            df.loc[len(df)]={'indice': nwid, 'vecteur': vectstr}
            df.to_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor_hsv.csv", index=False)           


# conn=mysql.connector.connect(host="localhost",user="root",password="",database="bank_of_faces")
# curs=conn.cursor()
# curs.execute('SELECT * FROM faces')
# rows = curs.fetchall()
# for row in rows:
#     remplissagecsvfichier(row[0],row[3])

# conn.close()
# remplissageparimg(13,"C:/Users/ASUS/Downloads/Paolo-Maldini.jpg")
