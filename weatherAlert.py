"""
This program checks for weather alerts from the National Weather Service.
It will play the long text initially then the headline for each subsequent
loop throughout the duration of the alert until it is canceled. New alerts
will re-trigger this program.
"""

from alertDisplay import alertDisplay
from colorOptions import *
from displayTime import displayTime
from fontOptions import *
from renderImg import renderImgAlertText
from runImages import *
from settings import *

import feedparser
import hashlib

lastAlerts = []
del lastAlerts[:]


def weatherAlerts():
    alertItems = [
    ]
    del alertItems[
        :
        ]
    alertFeeds = [
        'https://alerts.weather.gov/cap/wwaatmget.php?x=' + weatherAlertCode + '&y=0'
    ]
    for url in alertFeeds:
        alertFeed = feedparser.parse(url)
        alerts = alertFeed["items"]
        for alert in alerts:
            alertItems.append(alert)
        for alertItem in alertItems:
            alertText = alertItem["title"]
            alertType = ""
            if "warning" in (alert["title"].lower()):
                alertType = "warning"
            elif "advisory" in (alert["title"].lower()):
                alertType = "advisory"
            elif "watch" in (alert["title"].lower()):
                alertType = "watch"
            else:
                if "warning" in (alert["summary"].lower()):
                    alertType = "warning"
                elif "advisory" in (alert["summary"].lower()):
                    alertType = "advisory"
                elif "watch" in (alert["summary"].lower()):
                    alertType = "watch"
                else:
                    alertType = "statement"
            # Check if there is an active alert by seeing if "There are no active watches, warnings or advisories" does not exist
            if "There are no active watches, warnings or advisories" in alertText:
                del lastAlerts[:]
            else:
                # Turn the last updated date and time into a MD5 value
                weatherAlertCurrent = (hashlib.md5(str(alertItem).encode('utf-8')).hexdigest())
                if weatherAlertCurrent not in lastAlerts:
                    lastAlerts.append(weatherAlertCurrent)
                    # Checks if this is still the current alert or a new alert based on the last updated date and time MD5 and displays full message if first run or brief message
                    alertDisplay(alertType)
                    alertText = "Weather Alert - Urgency: " + alertItem["cap_urgency"] + " - Severity: " + alertItem["cap_severity"] + " - " + alertItem["title"] + " - " + alertItem["summary"]
                else:
                    alertText = "Weather Alert: " + alertItem["title"]
                if alertType == "other":
                    alertText = alertText + " " + alertItem["summary"]
                # Renders the text to the image
                renderImgAlertText("weatherAlertText.png", alertText, alertFont, backgroundColor, 0, 0, alertType)
                for x in range(0, 2):
                    displayTime(0)
                    scrollImgDisplay("weatherAlertText.png", 40)
