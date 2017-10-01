import urllib
import cv2
import numpy as np
import scipy
from PIL import Image
from scipy import misc
import requests
cascPath = "haarcascade_frontalface_default.xml"

def readUrlAndReturnArray(url):
	url_response = urllib.urlopen(url)
	img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
	img = cv2.imdecode(img_array, -1)
	return img

def crop_greyscale_resize_and_save (faces_and_original,imagePixels):
    faceList=[]
    for (x, y, w, h) in faces_and_original:
        cropped_example = imagePixels[y: y + h, x: x + w]
        faceList.append(cropped_example)
    return np.asarray(faceList)

def find_faces (imageArray):
    faceCascade = cv2.CascadeClassifier(cascPath)
    gray = cv2.cvtColor(imageArray, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )
    print ("Found {0} faces!".format(len(faces)))
    return (faces)

def mainFunction(url):
	imagePixels=readUrlAndReturnArray(url)	
	faces=find_faces(imagePixels)
	cropped_example= crop_greyscale_resize_and_save(faces,imagePixels)
	return cropped_example
    
x=mainFunction("http://img.src.ca/2016/01/08/635x357/160108_no0lk_rci-m-face-1_sn635.jpg")
#import pickle
#pickle.dump(x,open("multipleFaces.p","wb"))
print type(x)