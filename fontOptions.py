"""
The font definitions are stored in this file
"""

from PIL import ImageFont

# Font definitions
mainTTF = "VCR_OSD_MONO_1.001.ttf"
weatherTTF = "arial.ttf"
mainSize = 19
mainFont = ImageFont.truetype(mainTTF, mainSize)

newsSize = 25
newsFont = ImageFont.truetype(mainTTF, newsSize)

weatherSizeSmall = 14
weatherFontSmall = ImageFont.truetype(weatherTTF, weatherSizeSmall)

weatherSize = 14
weatherFont = ImageFont.truetype(weatherTTF, weatherSize)

alertFontSize = 24
alertFont = ImageFont.truetype(mainTTF, alertFontSize)

