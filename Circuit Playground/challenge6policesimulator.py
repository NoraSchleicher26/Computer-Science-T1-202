from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run
import time     #Import time for program to be able to run on time durations
cp.pixels.brightness = 0.1      #Turns brightness down


while True:     #Has program run the entire time
    cp.pixels.fill ((255,0,0))      #Turns all pixels to red
    cp.play_tone(500,0.5)       #Plays frequency of 500Hz for 0.5 seconds
    time.sleep(0.5)     #Waits a duration of 0.5 seconds
    cp.pixels.fill ((0,0,255))      #Turns all pixels to blue
    cp.play_tone(900,0.5)       #Plays frequency of 900Hz for 0.5 seconds
    time.sleep(0.5)     #Waits a duration of 0.5 seconds