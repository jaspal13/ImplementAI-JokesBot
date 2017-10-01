import sys
import os
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

folder = sys.argv[1]

#Loops through a folder of images
def loop_through_folder():
    suffix = "jpg"
    for fn in os.listdir(folder):
        if fn.endswith(suffix):
            decide_if_face(fn)

def decide_if_face (file_name):
    image = plt.imshow(mpimg.imread(folder +'/' + file_name))
    plt.ion()
    plt.show()
    answer = input("Is this a face[y/n]: ")
    if answer.lower() != "y":
            os.remove(folder+'/'+file_name)
    plt.close()

loop_through_folder()
