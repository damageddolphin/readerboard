"""
This program is to load the weather forecast. It will parse the JSON data into a dict and send it
to the main program to display on the board.
"""

import json
import urllib.request

from colorOptions import *
from displayTime import displayTime
from fontOptions import *
from renderImg import renderImg
from runImages import *
from settings import obsUrl


def weatherForecast():
    urllib.request.urlretrieve(obsUrl, 'weatherForecast.json')

    with open('weatherForecast.json') as json_file:
        data = json.load(json_file)

    dictLen = len(data['time']) - 1
    n = 0
    weatherForecast = []

    for w in data:
        dayString = data['time']['startPeriodName'][n]
        textString = data['data']['text'][n]
        weatherString = dayString + " " + textString + "\n"
        weatherForecast.append(weatherString)
        n = n + 1

    return (weatherForecast)


def displayForecast(title):
    weatherForecast = title + "          "
    renderImg("weatherForecast.png", weatherForecast, alertFont, backgroundColor, 0, 0)
    for x in range(0, 1):
        scrollImgDisplay('weatherForecast.png', 40)


def runForecast(timeCycle):
    forecastItems = weatherForecast()
    for item in forecastItems:
        timeCycle = displayTime(timeCycle)
        displayForecast(item)
