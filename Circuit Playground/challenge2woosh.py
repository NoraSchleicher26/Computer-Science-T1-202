from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run
import time     #Importing time for code to run on 367ms repetitions




cp.pixels.brightness = 0.01     #Turning down brightness of pixels


while True:
    if cp.button_a:     #Having program run if button is on
        leds = [0,1,2,3,4,5,6,7,8,9]        #Setting up list
        for led in leds:        #Starting for loop
            cp.pixels[led] = (0, 0, 255)        #Having all LEDS turn blue
            time.sleep(0.1)     #Waiting 100ms
            cp.pixels[led] = (0, 0, 0)      #Having all LEDS turn off
    else:       #Showing what happens if button is off
        cp.pixels.fill((0,0,0))     #Turning off all LEDS