#!/usr/bin/python

from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

# Test inverse on & off
printer.inverseOn()
printer.println("Inverse ON")
printer.inverseOff()

# Test character double-height on & off
printer.doubleHeightOn()
printer.boldOn()
printer.justify('L')

printer.println("STUDIO-X NEW YORK")


# Print the 75x75 pixel logo in adalogo.py
# import gfx as img
#printer.printBitmap(img.width, img.height, img.data)


printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults
