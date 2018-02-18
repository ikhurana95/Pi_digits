#!/usr/bin/env python


from picamera import PiCamera
from time import sleep
import numpy as np
from PIL import Image

def shoot(index):
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('/pics/pic%s.jpg' % index)
    camera.stop_preview()

'''
img = Image.open('orig.png').convert('RGBA')
arr = np.array(img)

# record the original shape
shape = arr.shape

# make a 1-dimensional view of arr
flat_arr = arr.ravel()

# convert it to a matrix
vector = np.matrix(flat_arr)
'''


shoot(1)