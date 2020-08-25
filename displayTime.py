"""
This module displays the date and time at the top of the board.
At the start of the program and at every hour, Sonic runs across.
"""

import time

from fontOptions import *
from colorOptions import *
from hourlyChime import *
from nightCheck import nightCheck
from renderImg import renderImg
from runImages import *
from settings import *

global chimeRan
chimeRan = 0


def displayTime(timeCycle):
    # Display animation every hour except quiet hours
    nightMode = nightCheck()
    global chimeRan
    if nightMode is False:
        if chimeRan != time.strftime('%H'):
            animationDisplay()
            chimeRan = time.strftime('%H')

    # Display time on top of board
    localTime = time.strftime('%-I:%M %p')
    localDate = time.strftime('%m/%d/%y')
    if timeCycle is 0:
        clockDisp = localDate
    if timeCycle is 1:
        clockDisp = localTime
    if timeCycle is 0:
        timeCycle = 1
    else:
        timeCycle = 0
    renderImg("time.png", clockDisp, mainFont, backgroundColor, 0, -3)
    imageDisplay("time.png", 4, 0)
    return (timeCycle)
