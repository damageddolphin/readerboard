"""
This program loads the current weather observations.
It is called from the main program by each section depending what information will be displayed.
eg: temp, humidity, and so on. Sometimes the reporting station is not reporting a value so it will
return None.
"""

from colorOptions import *
from displayTime import displayTime
from fontOptions import *
from renderImg import renderImg
from runImages import *
from settings import *

import datetime
import os
import urllib.request
import xml.etree.ElementTree as ET
import xmltodict


def loadWeather():
    urllib.request.urlretrieve(weatherObservationURL, 'weatherObservations.xml')

    global tree
    global root
    tree = ""
    root = ""
    tree = ET.ElementTree(file='weatherObservations.xml')
    root = tree.getroot()


# Displays "Weather"
def weatherMessage():
    currentObservation = "Your Local Weather"
    renderImg("WXObs.png", currentObservation, weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('WXObs.png', 2)


# Displays when weather information was last updated
def weatherLastObs():
    weatherTest = root.find('observation_time_rfc822')
    if weatherTest is not None:
        observationTime = root.find('observation_time_rfc822').text
        observationTime = observationTime[:-9]
        observationTime = datetime.datetime.strptime(observationTime, '%a, %d %b %Y %H:%M').strftime(
            '%m/%d/%y %-I:%M %p')
    else:
        observationTime = "Unknown"
    renderImg("WXObs.png", "Last Updated", weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('WXObs.png', 2)
    renderImg("CurrObs.png", observationTime, weatherFontSmall, backgroundColor, 0, 0)
    scrollImgDispUp('CurrObs.png', 2)


# Displays sky conditions
def weatherSky():
    weatherTest = root.find('weather')
    if weatherTest is not None:
        currentSkys = root.find('weather').text
    else:
        currentSkys = "Not Reported"
    renderImg("WXObs.png", "Sky Conditions", weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('WXObs.png', 2)
    renderImg("CurrObs.png", currentSkys, weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('CurrObs.png', 2)


# Displays temperature
def weatherTemperature():
    weatherTest = root.find('temperature_string')
    if weatherTest is not None:
        currentTemperature = root.find('temperature_string').text
    else:
        currentTemperature = "Not Reported"
    renderImg("WXObs.png", "Temperature", weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('WXObs.png', 2)
    renderImg("CurrObs.png", currentTemperature, weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('CurrObs.png', 2)


# Displays dewpoint
def weatherDewpoint():
    weatherTest = root.find('dewpoint_string')
    if weatherTest is not None:
        currentDewpoint = root.find('dewpoint_string').text
    else:
        currentDewpoint = "Not Reported"
    renderImg("WXObs.png", "Dewpoint", weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('WXObs.png', 2)
    renderImg("CurrObs.png", currentDewpoint, weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('CurrObs.png', 2)


# Displays heat index
def weatherHeatIndex():
    weatherTest = root.find('heat_index_string')
    if weatherTest is not None:
        currentHeatIndex = root.find('heat_index_string').text
    else:
        currentHeatIndex = "Not Reported"
    renderImg("WXObs.png", "Heat Index", weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('WXObs.png', 2)
    renderImg("CurrObs.png", currentHeatIndex, weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('CurrObs.png', 2)


# Displays wind speed and direction
def weatherWinds():
    currentWindDir = root.find('wind_dir')
    currentWindSpd = root.find('wind_mph')
    if currentWindDir is not None and currentWindSpd is not None:
        currentWind = root.find('wind_dir').text
        currentWind = currentWind + " " + root.find('wind_mph').text + " mph"
    else:
        currentWind = "Not Reported"
    renderImg("WXObs.png", "Winds", weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('WXObs.png', 2)
    renderImg("CurrObs.png", currentWind, weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('CurrObs.png', 2)


# Displays wind gust speed
def weatherGusts():
    currentWindGusts = root.find('wind_gust_mph')
    if currentWindGusts is not None:
        currentWindGusts = root.find('wind_gust_mph').text + " mph"
    else:
        currentWindGusts = "None"
    renderImg("WXObs.png", "Wind Gusts", weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('WXObs.png', 2)
    renderImg("CurrObs.png", currentWindGusts, weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('CurrObs.png', 2)


# Displays humidity
def weatherHumidity():
    currentHumidityTest = root.find('relative_humidity')
    if currentHumidityTest is not None:
        currentHumidity = root.find('relative_humidity').text + " %"
    else:
        currentHumidity = "Not Reported"
    renderImg("WXObs.png", "Humidity", weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('WXObs.png', 2)
    renderImg("CurrObs.png", currentHumidity, weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('CurrObs.png', 2)


# Displays barometric pressure in inches
def weatherBarometer():
    currentPressureTest = root.find('pressure_in')
    if currentPressureTest is not None:
        currentPressure = root.find('pressure_in').text + "\""
    else:
        currentPressure = "Not Reported"
    currentPressureTest = root.find('pressure_mb')
    if currentPressureTest is not None:
        currentPressure = currentPressure + " (" + root.find('pressure_mb').text + "mb)"
    renderImg("WXObs.png", "Barometer", weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('WXObs.png', 2)
    renderImg("CurrObs.png", currentPressure, weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('CurrObs.png', 2)


# Displays visibility
def weatherVisibility():
    currentVisibilityTest = root.find('visibility_mi')
    if currentVisibilityTest is not None:
        currentVisibility = root.find('visibility_mi').text + " mi"
    else:
        currentVisibility = "Not Reported"
    renderImg("WXObs.png", "Visibility", weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('WXObs.png', 2)
    renderImg("CurrObs.png", currentVisibility, weatherFont, backgroundColor, 0, 0)
    scrollImgDispUp('CurrObs.png', 2)


# Displays credit
def weatherCredit():
    weatherCreditTest = root.find('credit')
    os.remove('weatherObservations.xml')
    if weatherCreditTest is not None:
        weatherCredit = "Weather courtesy of " + root.find(
            'credit').text + "             ...... and now your local forecast     "
        renderImg("WXObs.png", weatherCredit, mainFont, backgroundColor, 0, 0)
        scrollImgDisplay('WXObs.png', 42)
