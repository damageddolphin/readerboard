"""
This program checks if it is night time hours
"""
import time
from settings import *


def nightCheck():
    currentHour = int(time.strftime('%H'))
    if quietStart < quietEnd:
        if quietStart <= currentHour and quietEnd > currentHour:
            return (True)
        else:
            return (False)
    elif quietEnd < quietStart:
        if currentHour >= quietStart or currentHour < quietEnd:
            return (True)
        else:
            return (False)
