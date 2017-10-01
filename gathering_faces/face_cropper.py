import cv2
import sys
import os
from PIL import Image

# The cascPath is the file that contains the data for creating the haar cascade
# that contains data to indentify faces
cascPath = "haarcascade_frontalface_default.xml"

# Source is the folder that contains the pictures from which we want to get faces
source = sys.argv[1]
#Destination is where the pictures will go
destination = sys.argv[2]


# Finds faces in an image
# Returns list of faces
def find_faces (image_path, iteration):
    # Create the haar cascade in open CV
    original_image = Image.open(image_path)
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )
    print ("Found {0} faces!".format(len(faces)))

    return (faces, original_image, image_path, iteration)

#For each face found, crops the face, makes it greyscale and resizes it
def crop_greyscale_resize_and_save (faces_and_original):
    faces = faces_and_original[0]
    original_image = faces_and_original[1]
    image_path = faces_and_original[2]
    iteration = faces_and_original[3]
    j = 0
    for (x, y, w, h) in faces:
        left = x
        top = y
        right = (x + w)
        bottom = (y + h)
        cropped_example = original_image.crop((left, top, right, bottom))
        #Converts it to greyscale
        cropped_example = cropped_example.convert('L')
        #Resizes it to 48*48, the format our machine learning model needs
        cropped_example = cropped_example.resize((48,48))
        final_path = destination + '/' + str(iteration) + '+' + str(j) + ".jpg"
        cropped_example.save (final_path)
        j += 1

#Loops through a source folder of images
def loop_through_folder():
    iteration = 0
    suffix = "jpg"
    for fn in os.listdir(source):
        if fn.endswith(suffix):
            iteration += 1
            crop_greyscale_resize_and_save(find_faces(source+'/'+fn, iteration))

loop_through_folder()
