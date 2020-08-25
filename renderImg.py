"""
This program takes the text and renders the image. There are three different
renderers for three different types of text.
"""

from colorOptions import *
from fontOptions import *
from runImages import *

from PIL import Image
from PIL import ImageDraw
import os
import time


def renderImg(imgName, imgText, imgFont, imgBackground, imgX, imgY):
    w, h = imgFont.getsize(imgText)
    h = h * 2
    w = w + 2
    image = Image.new('RGB', (w, h), imgBackground)
    draw = ImageDraw.Draw(image)
    draw.text((imgX, imgY), imgText, fill=randomColors(), font=imgFont)
    save_location = os.getcwd()
    image.save(save_location + '/' + imgName)


def renderImgAlert(imgName, imgText, imgFont, imgBackground, imgX, imgY, alertType):
    fill = alertColors(alertType)
    w = 128
    h = 64
    image = Image.new('RGB', (w, h), imgBackground)
    draw = ImageDraw.Draw(image)
    draw.text((imgX, imgY), imgText, fill, font=imgFont)
    save_location = os.getcwd()
    image.save(save_location + '/' + imgName)
    imageDisplay(imgName, 0, 0)
    time.sleep(0.5)
    image = Image.new('RGB', (w, h), fill)
    draw = ImageDraw.Draw(image)
    draw.text((imgX, imgY), imgText, imgBackground, font=imgFont)
    save_location = os.getcwd()
    image.save(save_location + '/' + imgName)
    imageDisplay(imgName, 0, 0)
    time.sleep(0.5)


def renderImgAlertText(imgName, imgText, imgFont, imgBackground, imgX, imgY, alertType):
    fill = alertColors(alertType)
    w, h = imgFont.getsize(imgText)
    h = h * 2
    image = Image.new('RGB', (w, h), imgBackground)
    draw = ImageDraw.Draw(image)
    draw.text((imgX, imgY), imgText, fill, font=imgFont)
    save_location = os.getcwd()
    image.save(save_location + '/' + imgName)
