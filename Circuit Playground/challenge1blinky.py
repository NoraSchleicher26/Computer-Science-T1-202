#Imports the tools needed to interact with the board
from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run
import time     #Importing time for code to run on 367ms repetitions


cp.pixels.brightness = 0.01     #Turning down brightness of pixels

#Everything that you write will go inside the while true loop

while True:
    cp.pixels.fill  ((0, 255, 0))      #Changing the LEDS to green only
    time.sleep(0.367)       #Waits 367ms
    cp.pixels.fill  ((0, 0, 0))     #Turns all LEDS off
    time.sleep(0.367)       #Waits 367ms