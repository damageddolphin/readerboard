import time
import importlib
import configparser
from settings import *
from nightCheck import nightCheck

backgroundColor = (0, 0, 0)
maxBrightness = 255

"""
This portion taken from hzeller/rpi-rgb-led-matrix pulsing-colors
and modified to work with this program to fades through the colors
"""

# This section is for normal running colors
def randomColors():
    # Night mode check
    nightMode = nightCheck()

    config = configparser.ConfigParser()
    config.read("colorValues.py")
    colorOld = int(config.get("colorVars", "colorOld"))

    continuum = colorOld
    colorReplace = colorOld

    continuum += colorSteps
    continuum %= 3 * 255
    colorNew = continuum

    with open('colorValues.py', 'r+') as variableFile:
        content = variableFile.read()
        variableFile.seek(0)
        variableFile.truncate()
        variableFile.write(content.replace("colorOld=" + str(colorReplace), "colorOld=" + str(colorNew)))
    colorReplace = colorNew

    red = 0
    green = 0
    blue = 0

    if continuum <= 255:
        c = continuum
        blue = 255 - c
        red = c
    elif continuum > 255 and continuum <= 511:
        c = continuum - 256
        red = 255 - c
        green = c
    else:
        c = continuum - 512
        green = 255 - c
        blue = c

    if nightMode is True:
        if red > 50:
            red = int(red * 0.1)
        if green > 40:
            green = int(green * 0.1)
        if blue > 40:
            blue = int(blue * 0.1)
    return (red, green, blue)


# This section for the Weather Alert colors
def alertColors(alertType):
    nightMode = nightCheck()
    if nightMode is False:
        if alertType == "watch":
            alertRed = 255
            alertGreen = 155
            alertBlue = 0
        if alertType == "advisory":
            alertRed = 255
            alertGreen = 255
            alertBlue = 0
        if alertType == "warning":
            alertRed = 255
            alertGreen = 0
            alertBlue = 0
        if alertType == "statement":
            alertRed = 0
            alertGreen = 255
            alertBlue = 0
    if nightMode is True:
        if alertType == "watch":
            alertRed = 35
            alertGreen = 35
            alertBlue = 0
        if alertType == "advisory":
            alertRed = 42
            alertGreen = 13
            alertBlue = 0
        if alertType == "warning":
            alertRed = 42
            alertGreen = 0
            alertBlue = 0
        if alertType == "statement":
            alertRed = 0
            alertGreen = 42
            alertBlue = 0
    return (alertRed, alertGreen, alertBlue)
