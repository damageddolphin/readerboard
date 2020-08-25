from colorOptions import *
from fontOptions import *
from renderImg import renderImgAlert
"""
This is to generate the "ALERT" message in the color associated with the type of alert.
The text is received and sent to the image renderer
"""
def alertDisplay(alertType):
    for disp in range(0,10):
        alertMessage = "WEATHER\n" + alertType.upper()
        alertFileName = "weatherAlert.png"
        renderImgAlert(alertFileName, alertMessage, alertFont, backgroundColor, 0, 7, alertType)


