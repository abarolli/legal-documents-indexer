
from pathlib import Path
from pprint import pprint
import cv2
import numpy as np

from PIL import Image


def preprocess_image(img:Image):
    img_arr = np.asarray(img) #convert image to matrix
    img_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY) #convert to grayscale before binarzation
    ret, imgf = cv2.threshold(img_arr, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #binarize using Otsu's algorithm
    img = Image.fromarray(imgf)
    return img