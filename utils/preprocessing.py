import cv2
import numpy as np

def preprocess_image(image_path):
    image=cv2.imread(image_path)
    image=cv2.resize(image,(224,224))
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    equalized=cv2.equalizeHist(blur)
    normalized=equalized/255.0
    return normalized

def load_image(image_path):
    image=cv2.imread(image_path)
    image=cv2.resize(image,(224,224))
    image=image/255.0
    return image