from displayTime import displayTime
from loadNews import *
from networkCheck import networkCheck
from weatherAlert import *
from weatherObservations import *
from weatherForecast import *
from setup import *

# Counters to queue the date and time display switch and when to run the weather program.
timeCycle = 0
runWeather = 0


# This section runs the current weather conditions while switching between date and time
def displayWeather(timeCycle):
    loadWeather()
    timeCycle = displayTime(timeCycle)
    weatherMessage()
    timeCycle = displayTime(timeCycle)
    weatherLastObs()
    timeCycle = displayTime(timeCycle)
    weatherSky()
    timeCycle = displayTime(timeCycle)
    weatherTemperature()
    timeCycle = displayTime(timeCycle)
    weatherDewpoint()
    timeCycle = displayTime(timeCycle)
    weatherHeatIndex()
    timeCycle = displayTime(timeCycle)
    weatherWinds()
    timeCycle = displayTime(timeCycle)
    weatherGusts()
    timeCycle = displayTime(timeCycle)
    weatherHumidity()
    timeCycle = displayTime(timeCycle)
    weatherBarometer()
    timeCycle = displayTime(timeCycle)
    weatherVisibility()
    timeCycle = displayTime(timeCycle)
    weatherCredit()


# This is the main running program. It calls the news, weather alerts, and weather.
while True:
    networkCheck()
    items = loadNews()
    for item in items:
        timeCycle = displayTime(timeCycle)
        weatherAlerts()
        if runWeather == weatherDisplay:
            displayWeather(timeCycle)
            runForecast(timeCycle)
            runWeather = 0
        runWeather = runWeather + 1
        newsHeadline = item["title"]
        displayNews(newsHeadline, timeCycle)
