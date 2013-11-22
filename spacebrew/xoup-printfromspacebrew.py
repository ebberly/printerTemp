
#imports are from spacebrew example..
import time
import locale
import sys
from pySpacebrew.spacebrew import Spacebrew

# imports from adafruit printer
from Adafruit_Thermal import *

# create a new printer instance
printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

# set printer formats
printer.doubleHeightOn()
printer.boldOn()
printer.justify('L')
printer.println("Printer on")
printer.feed(5)


# get app name and server from query string
name = "Xoup Printer"
server = "server.sitetosite.co"

# add subscriber
brew = Spacebrew(name, server=server)
brew.addSubscriber("incoming strings", "string")


def handleString(value):
	printer.println(value)	
	printer.feed(2)




brew.subscribe("incoming strings", handleString)

brew.start()

filepath = "test.gif"

buffer = open(filepath, 'rb').read()

printer.printBitmap(100, 100, buffer)