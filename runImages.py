"""
This program displays the rendered images on the LED board.
Each one is for the different type of display.
"""

import time
from PIL import Image
from matrixOptions import *
from settings import *

# This module brings image up and exits to the left. It is used for the current weather.
def scrollImgDispUp( imgFile, holdX ):
    image = Image.open(imgFile)
    image.load()
    for yPlace in range(pYrange, 12, -1):
        matrix.SetImage(image, holdX, yPlace)
        time.sleep(anSpeedUp)
        holdY = yPlace
    time.sleep(1)
    for n in range(0, -image.size[0], -1):
        matrix.SetImage(image, n, holdY)
        time.sleep(anSpeedUp)

# This module scrolls the image across the board right to left. holdY is the Y position it will scroll across.
def scrollImgDisplay( imgFile, holdY ):
    image = Image.open(imgFile)
    image.load()
    for n in range(128, -image.size[0], -1):
        matrix.SetImage(image, n, holdY)
        time.sleep(anSpeedScroll)

# This module displays an image statically.
def imageDisplay(imageFile, dispX, dispY):
    image = Image.open(imageFile)
    image.load()
    matrix.Clear()
    matrix.SetImage(image, dispX, dispY)

# This module is for the loading message. It is the same as imageDisplay() but does not clear the display
def imageLoading(imageFile, dispX, dispY):
    image = Image.open(imageFile)
    image.load()
    matrix.SetImage(image, dispX, dispY)

