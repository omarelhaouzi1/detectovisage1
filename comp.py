import numpy as np
from numpy import dot
import pandas as pd
def compareVect(vect1):
    indice=-1
    dis_min = float('inf')
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor1.csv")
    vect1=vect1 /(np.linalg.norm(vect1)+1e-8)
    for f in df.itertuples():
        vect = np.array([float(x) for x in f.vecteur.split()])
        vect=vect /(np.linalg.norm(vect)+1e-8)
        dis=np.linalg.norm(vect1-vect)
        if dis<dis_min:
            dis_min=dis
            indice=f.indice
    print(dis_min)
    print(indice) 
    if dis_min < 0.62:
        print(indice) 
        print(dis_min)
        return indice
    return -1
def comparehsvVect(vect1):
    indice=-1
    dis_min = float('inf')
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor_hsv.csv")
    vect1=vect1 /(np.linalg.norm(vect1)+1e-8)
    for f in df.itertuples():
        vect = np.array([float(x) for x in f.vecteur.split()])
        vect=vect /(np.linalg.norm(vect)+1e-8)
        dis=np.linalg.norm(vect1-vect)
        if dis<dis_min:
            dis_min=dis
            indice=f.indice
    print(indice)
    print(dis_min)    
    if dis_min <0.6: 
        
        return indice
    return -1
def comparelbpVect(vect1):
    indice=-1
    dis_min = float('inf')
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor_lbp.csv")
    for f in df.itertuples():
        vect = np.array([float(x) for x in f.vecteur.split()])
        dis=np.linalg.norm(vect1-vect)
        print(dis)
        if dis<dis_min:
            dis_min=dis
            indice=f.indice
    print(dis_min)       
    if dis_min <0.037: 
        return indice
    return -1
def comparehogVect(vect1):
    indice=-1
    dis_min = float('inf')
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor_hog.csv")
    for f in df.itertuples():
        vect = np.array([float(x) for x in f.vecteur.split()])
        dis=np.linalg.norm(vect1-vect)
        if dis<dis_min:
            dis_min=dis
            indice=f.indice   
    print(indice)
    print(dis_min)
    if dis_min <0.65: 
        return indice
    return -1

def compareVect_cosine(vect1):
    df=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Reconnaissance facial/haarcascade/Bank_of_descriptor_hsv.csv")
    max_sim = -1
    indice = -1
    vect1=vect1/(np.linalg.norm(vect1)+1e-8)
    for f in df.itertuples():
        vect2 = np.array([float(x) for x in f.vecteur.split()])
        vect2=vect2/(np.linalg.norm(vect2)+1e-8)
        sim = dot(vect1, vect2)
        if sim > max_sim:
            max_sim = sim
            indice = f.indice
    print(indice)
    print(sim)
    if max_sim > 0.95:  
        print("Similarité cosinus:", max_sim)
        return indice
    return -1