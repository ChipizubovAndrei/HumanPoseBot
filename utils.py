import glob
import os

def clearup_images(pathToImages):
    image_type = ['*.jpg', '*.jpeg', '*.png']
    for imtype in image_type:
        files = glob.glob(pathToImages + imtype)
        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))