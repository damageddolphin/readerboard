"""
This is the hourly animation program. It displays a series of images across the board.
It is hard coded to work with the Sonic images. Adjustments would need to be made to
the y values which are distance traveled. Change sonicFrame < 8 value to the total
number of frames the new animation has.
"""
from runImages import *

def animationDisplay():
    matrix.Clear()
    sonicRun = 0
    sonicFrame = 0
    y = 0
    while y < 70:
        sonicFrame = 0
        if sonicRun >= 100:
            sonicRun = 0
            y = y + 15
        while sonicFrame < 8:
            animationFrame = 'animation/SonicRun-' + str(sonicFrame) + '.jpg'
            imageDisplay(animationFrame, sonicRun, y)
            time.sleep(0.05)
            sonicRun = sonicRun + 6
            sonicFrame = sonicFrame + 1

