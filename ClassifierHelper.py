import os
from PIL import Image


for fn in os.listdir('.'):
    if os.path.isfile(fn) and fn.endswith (.jpg):
        img = Image.open(fn)
        img.show()
