# -*- coding: utf-8 -*-
"""
This module loads the news headlines from RSS feeds and returns
them to the main program to render for display.
It will calculate a percentage based on the total of feeds and
create a Loading message. Any headlines which have a word included
in the exclude list will be excluded.
"""
from colorOptions import *
from displayTime import displayTime
from fontOptions import *
from renderImg import renderImg
from runImages import *
from settings import *

import feedparser


def loadNews():
    items = []
    del items[:]
    countdown = len(feeds)
    loadingDots = ""
    countUp = 1
    displayTime(0)
    for url in feeds:
        print(url)
        perComp = float(countUp) / countdown
        countUp = countUp + 1
        loadingDots = loadingDots + u"\u2588"
        feed = feedparser.parse(url)
        posts = feed["items"]
        txtLoading = "Loading:" + str(int(perComp * 100)) + "%"
        renderImg("loading.png", txtLoading, mainFont, backgroundColor, 0, 0)
        imageLoading("loading.png", 0, 45)
        for post in posts:
            wordCheck = str(post)
            if not any(word in wordCheck for word in excludeList):
                items.append(post)
    return (items)


def displayNews(title, timeCycle):
    newsHeadline = title + "          "
    renderImg("news.png", newsHeadline, newsFont, backgroundColor, 0, 0)
    displayTime(timeCycle)
    for x in range(0, 2):
        scrollImgDisplay('news.png', 40)
