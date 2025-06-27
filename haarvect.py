import cv2
from skimage.feature import local_binary_pattern
import numpy
from scipy.stats import skew,kurtosis
from hogvect import *
import os
def momentlbp(chemin_image,rad=1,nb=8):
    lpbmm=[]
    if type(chemin_image)==str:
        image=cv2.imread(chemin_image)
    else:
        image=chemin_image
    if len(image.shape)==3:
        img1=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    else:
        img1=image
    img1 = cv2.resize(img1, (128, 128))
    lbp=local_binary_pattern(img1,rad,nb,method='uniform')
    hist,bin=numpy.histogram(lbp.ravel(),bins=numpy.arange(0, nb + 3),range=(0, nb + 2))
    hist = hist.astype("float")
    hist /= (hist.sum() + 1e-7)
    my=numpy.mean(hist)
    var=numpy.var(hist)
    sk = skew(hist)           
    kurt = kurtosis(hist)     
    lpbmm.extend([my, var, sk, kurt])
    return  numpy.array(lpbmm)
def vecteur_lbp_complet(chemin_image, rad=1, nb=8):
    if type(chemin_image)==str:
        image=cv2.imread(chemin_image)
    else:
        image=chemin_image
    
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    lbp = local_binary_pattern(image, nb, rad, method='uniform')
    
    n_bins = int(lbp.max() + 1) 
    hist, _ = np.histogram(lbp.ravel(), bins=n_bins, range=(0, n_bins))

    # Normalisation
    hist = hist.astype("float")
    hist /= (hist.sum() + 1e-7)

    return hist
# def hsv(chemin_image):
#     if type(chemin_image)==str:
#         image=cv2.imread(chemin_image)
#     else:
#         image=chemin_image
#     img=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
#     h,s,v=cv2.split(img)
#     mmts=[]
#     for i ,ch in enumerate([h,s,v]):
        
#         ch_normalise=ch.astype(numpy.float64)
#         if i==0:
#             ch_normalise /= 180.0
#         else:
#             ch_normalise /= 255.0 
#         my=numpy.mean(ch_normalise)
#         var=numpy.var(ch_normalise)
#         sk = skew(ch_normalise.flatten())           
#         kurt = kurtosis(ch_normalise.flatten()) 
#         mmts.extend([my,var,sk,kurt])
#     return numpy.array(mmts) 
def hsv(chemin_image,bins=8):
    if type(chemin_image)==str:
      image=cv2.imread(chemin_image)
    else:
        image=chemin_image
    hsv_img=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_img)
    hist_h = cv2.calcHist([h], [0], None, [bins], [0, 180])
    hist_s = cv2.calcHist([s], [0], None, [bins], [0, 256])
    hist_v = cv2.calcHist([v], [0], None, [bins], [0, 256])

    # Concatène les histogrammes
    hist = np.concatenate([hist_h, hist_s, hist_v]).flatten()

    # Normalisation (L2)
    hist_norm = hist / np.linalg.norm(hist) if np.linalg.norm(hist) != 0 else hist

    return hist_norm
    

def vecteur(image):
    vect=numpy.concatenate([vecteur_lbp_complet(image),extract_hog_vector(image)])
    norm = numpy.linalg.norm(vect)
    if norm == 0:
        print("Vecteur nul, impossible de normaliser.") 
        return 0
    vect_normalise = vect/norm
    return vect_normalise











# def groupevecteur(chdossier):
#     listimg=[]
#     for img in os.listdir(chdossier):
#         chemin=os.path.join(chdossier,img)
#         if os.path.isfile(chemin):
#             v1=vecteur(chemin)
#             listimg.append(v1)
#     fvecteur=numpy.mean(numpy.array(listimg),axis=0)
#     return fvecteur
