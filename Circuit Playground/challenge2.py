from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run
import time     #Importing time for code to run on 367ms repetitions




cp.pixels.brightness = 0.01     #Turning down brightness of pixels


while True:
    if cp.button_a:
        leds = [0,1,2,3,4,5,6,7,8,9]
        for led in leds:
            cp.pixels[led] = (0, 0, 255)
            time.sleep(0.1)
            cp.pixels[led] = (0, 0, 0)
    else:
        cp.pixels.fill((0,0,0))