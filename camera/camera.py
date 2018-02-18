#!/usr/bin/env python


from picamera import PiCamera
from time import sleep


def shoot(index):
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('/pics/pic' + index + '.jpg')
    camera.stop_preview()
