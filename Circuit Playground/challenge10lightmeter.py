from adafruit_circuitplayground import cp     #Importing cp to allow code in playground to run
import time     #Import time for program to be able to run on time durations


while True:     #Having program run all the time
    if cp.light <= 30:      #Showing what happens if cp.light is less than or equal to 30
        cp.pixels[0] = (0,0,1)      #Pixel 0 is blue
    if cp.light <= 27:      #Showing what happens if cp.light is less than or equal to 27
        cp.pixels[1] = (0,0,1)      #Pixel 1 is blue
    if cp.light <= 24:      #Showing what happens if cp.light is less than or equal to 24
        cp.pixels[2] = (0,0,1)      #Pixel 2 is blue
    if cp.light <= 21:      #Showng what happens if cp.light is less than or equal to 21
        cp.pixels[3] = (0,0,1)      #Pixel 3 is blue
    if cp.light <= 18:      #Showing what happens if cp.light is less than or equal to 18
        cp.pixels[4] = (0,0,1)      #Pixel 4 is blue
    if cp.light <= 15:      #Showing what happens if cp.light is less than or equal to 15
        cp.pixels[5] = (0,0,1)      #Pixel 5 is blue
    if cp.light <= 12:      #Showing what happens if cp.light is less than or equal to 12
        cp.pixels[6] = (0,0,1)      #Pixel 6 is blue
    if cp.light <= 9:       #Showing what happens if cp.light is less than or equal to 9
        cp.pixels[7] = (0,0,1)      #Pixel 7 is blue
    if cp.light <= 6:       #Showing what happens if cp.light is less than or equal to 6
        cp.pixels[8] = (0,0,1)      #Pixel 8 is blue
    if cp.light <= 3:       #Showing what happens if cp.light is less than or equal to 3
        cp.pixels[9] = (0,0,1)      #Pixel 9 is blue
    if cp.light > 3:        #Showing what happens if cp.light is greater than 3
        cp.pixels[9] = (0,0,0)      #Pixel 9 is off
    if cp.light > 6:        #Showing what happens if cp.light is greater than 6
        cp.pixels[8] = (0,0,0)      #Pixel 8 is off
    if cp.light > 9:        #Showing what happens if cp.light is greater than 9
        cp.pixels[7] = (0,0,0)      #Pixel 7 is off
    if cp.light > 12:       #Showing what happens if cp.light is greater than 12
        cp.pixels[6] = (0,0,0)      #Pixel 6 is off
    if cp.light > 15:       #Showing what happens if cp.light is greater than 15
        cp.pixels[5] = (0,0,0)      #Pixel 5 is off
    if cp.light > 18:       #Showing what happens if cp.light is greater than 18
        cp.pixels[4] = (0,0,0)      #Pixel 4 is off
    if cp.light > 21:       #Showing what happens if cp.light is greater than 21
        cp.pixels[3] = (0,0,0)      #Pixel 3 is off
    if cp.light > 24:       #Showing what happens if cp.light is greater than 24
        cp.pixels[2] = (0,0,0)      #Pixel 2 is off
    if cp.light > 27:       #Showing what happens if cp.light is greater than 27
        cp.pixels[1] = (0,0,0)      #Pixel 1 is off
    if cp.light > 30:       #Showing what happens if cp.light is greater than 30
        cp.pixels[0] = (0,0,0)      #Pixel 0 is off
