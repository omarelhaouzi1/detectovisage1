import cv2
from skimage.feature import hog
import numpy as np
from scipy.stats import skew,kurtosis
def extract_hog_vector(image):
    hogmmts=[]
    if type(image)==str:
        img=cv2.imread(image)
    else:
        img=image
    if len(img.shape)==3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray=img
    gray = cv2.resize(gray, (128, 128)) 
    features = hog(
        gray,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        block_norm='L2-Hys',
        visualize=False,
        feature_vector=True
    )
    features = features / (np.linalg.norm(features) + 1e-8)
    return np.array(features)
   