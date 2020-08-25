"""
Since this device runs on WiFi, I have created a series of
network checks. It will detect if there is an issue with
the network and recommend what action to take.
"""
import os
import socket
import struct

from colorOptions import *
from fontOptions import *
from renderImg import renderImg
from runImages import *


# Get IP address of gateway / router
def localGateway():
    with open("/proc/net/route") as file:
        for line in file:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                continue
            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))


# Call this module to run program
def networkCheck():
    global gatewayIP
    global hostName
    global dnsIP

    gatewayIP = localGateway()
    hostName = "connectivitycheck.gstatic.com"
    dnsIP = "172.217.4.131"

    networkTest(gatewayIP, "gateway")
    networkTest(dnsIP, "internet")
    networkTest(hostName, "dns")


"""
This performs a series of ping tests against the addresses and should return a result of 0
Any non 0 result is an error and it will continue to attempt to restart the network interface
If after 5 attempts the network does not come back up a reboot will be initiated
"""


def networkTest(hostAddress, testName):
    testResponse = 1
    failCount = 0
    while testResponse is not 0:
        testResponse = os.system("ping -c 1 " + hostAddress)
        if testResponse is not 0:
            if failCount is 5:
                rebootSystem()
            errorMessage(testName)
            os.system('/sbin/ip link set eth0 down && /sbin/ip link set eth0 up')
            failCount = failCount + 1
            print(failCount)
    failCount = 0


# This scrolls the error message of what part of the network is not responding based on the results of the ping test.
def errorMessage(errorMessage):
    if errorMessage is "dns":
        errorMessage = "The DNS is down ... please check the DNS server.      "
    if errorMessage is "internet":
        errorMessage = "The Internet is down ... please check the router and modem.      "
    if errorMessage is "gateway":
        errorMessage = "The local network is down ... please check the router and modem.      "
    renderImg("networkError.png", errorMessage, newsFont, backgroundColor, 0, 0)
    scrollImgDisplay('networkError.png', 40)


# This scrolls a message twice a reboot is about to occur and then forces a reboot
def rebootSystem():
    networkError = "The network did not come back up - attempting to reboot ... please stand by          "
    renderImg("networkError.png", networkError, newsFont, backgroundColor, 0, 0)
    for x in range(0, 2):
        scrollImgDisplay('networkError.png', 40)
    os.system('sudo reboot')
