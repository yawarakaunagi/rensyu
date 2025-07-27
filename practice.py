import os
import glob
from PIL import Image


def get_files(folder):
    for file in glob.glob(folder):
        yield file



for file in get_files("C:/Users/katay/Documents/images/01/jpeg/*.jpg"):
    print(file)