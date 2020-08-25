"""
Do not modify this section
"""
from random import randint
from rgbmatrix import RGBMatrix, RGBMatrixOptions

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 64
options.chain_length = 4
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
options.led_rgb_sequence = "RBG"

matrix = RGBMatrix(options = options)

