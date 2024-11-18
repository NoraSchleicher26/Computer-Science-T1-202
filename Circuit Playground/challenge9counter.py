from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run
import time     #Import time for program to be able to run on time durations

presses = 0
while True:
    
    if cp.button_a:
        presses = presses + 1
        lights = [0,1,2,3,4,5,6,7,8,9]
        for light in lights: