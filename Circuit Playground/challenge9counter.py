from adafruit_circuitplayground import cp     #Importing cp to allow code in playground to run
import time     #Import time for program to be able to run on time durations


presses = 0       #Sets the variable for presses to -1
while True:     #Has function run all the time

   
    if cp.button_a:     #Shows what happens when button A is pressed
        if presses < 10:
            cp.pixels[presses] = (1,0,0)        #Turns on pixel variable by presses to red
            presses = presses + 1       #Increases presses variable by 1
  
            time.sleep(0.5)     #Waits 500ms


    if cp.button_b:     #Shows what happens when button B is pressed

            cp.pixels[presses] = (0,0,0)        #Turns of pixel variable by presses
            presses = presses  - 1      #Decreases presses variable by 1
            time.sleep(0.5)     #Waits 500ms