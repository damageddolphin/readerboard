"""
To look up your codes for weather alerts and weather forecast
visit https://alerts.weather.gov/
Scroll down to your state. Select County List for Forecast.
The county code can be used for the alert or if you prefer
more localized alerts go back and choose Zone List and
select a code which is closest to your location.

A word of warning: This should never be your primary means
of information for weather information.

News feeds are RSS sources. Copy and paste the URL to the RSS
link into the list encapsulated by quotes followed by a comma.
If there is any topic you wish to exclude, add that as a keyword
to the exclude list encapsulated by quotes followed by a comma.
Spatula is included as an example.
"""

weatherAlertCode='HIC003'
weatherForecastCode='HIZ005'
feeds=[
        "http://rss.reddit.com/r/news/new",
        "http://rss.reddit.com/r/newsoftheweird/new",
        "http://rss.reddit.com/r/nottheonion/new",
      ]
excludeList=[
         "Spatula",
        ]
weatherDisplay = 10
quietStart = 0
quietEnd = 7

# Do not make changes below
# Control elements for weather information
weatherObservationURL='http://w1.weather.gov/xml/current_obs/PHNL.xml'
obsUrl='https://forecast.weather.gov/MapClick.php?zoneid=' + weatherForecastCode + '&unit=0&lg=english&FcstType=json'
weatherAlertCheck='34dbb6665a32a0503d82c479c84e60b0'

# Defines parameters for the LED panel such as geometry, scroll speed, and how fast to step through colors
pYrange = 64
pXyrange = 128

anSpeedUp = 0.01
anSpeedScroll = 0.007

colorSteps = 1


