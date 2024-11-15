from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run
import time     #Import time for program to be able to run on time durations


while True:     #Has program run all the time
    import random
    diceroll = random.randint(1,11)
    if cp.button_a:
        if diceroll == 1:
            cp.pixels[0] = (0,0,255)
            cp.pixels[1] = (0,0,0)
            cp.pixels[2] = (0,0,0)
            cp.pixels[3] = (0,0,0)
            cp.pixels[4] = (0,0,0)
            cp.pixels[5] = (0,0,0)
            cp.pixels[6] = (0,0,0)
            cp.pixels[7] = (0,0,0)
            cp.pixels[8] = (0,0,0)
            cp.pixels[9] = (0,0,0)
            
            

        if diceroll == 2:
            cp.pixels[0] = (0,0,255)
            cp.pixels[1] = (0,0,255)
            cp.pixels[2] = (0,0,0)
            cp.pixels[3] = (0,0,0)
            cp.pixels[4] = (0,0,0)
            cp.pixels[5] = (0,0,0)
            cp.pixels[6] = (0,0,0)
            cp.pixels[7] = (0,0,0)
            cp.pixels[8] = (0,0,0)
            cp.pixels[9] = (0,0,0)
            
        if diceroll == 3:
            cp.pixels[0] = (0,0,255)
            cp.pixels[1] = (0,0,255)
            cp.pixels[2] = (0,0,255)
            cp.pixels[3] = (0,0,0)
            cp.pixels[4] = (0,0,0)
            cp.pixels[5] = (0,0,0)
            cp.pixels[6] = (0,0,0)
            cp.pixels[7] = (0,0,0)
            cp.pixels[8] = (0,0,0)
            cp.pixels[9] = (0,0,0)
           
        if diceroll == 4:
            cp.pixels[0] = (0,0,255)
            cp.pixels[1] = (0,0,255)
            cp.pixels[2] = (0,0,255)
            cp.pixels[3] = (0,0,255)
            cp.pixels[4] = (0,0,0)
            cp.pixels[5] = (0,0,0)
            cp.pixels[6] = (0,0,0)
            cp.pixels[7] = (0,0,0)
            cp.pixels[8] = (0,0,0)
            cp.pixels[9] = (0,0,0)
          
        if diceroll == 5:
            cp.pixels[0] = (0,0,255)
            cp.pixels[1] = (0,0,255)
            cp.pixels[2] = (0,0,255)
            cp.pixels[3] = (0,0,255)
            cp.pixels[4] = (0,0,255)
            cp.pixels[5] = (0,0,0)
            cp.pixels[6] = (0,0,0)
            cp.pixels[7] = (0,0,0)
            cp.pixels[8] = (0,0,0)
            cp.pixels[9] = (0,0,0)
           
        if diceroll == 6:
            cp.pixels[0] = (0,0,255)
            cp.pixels[1] = (0,0,255)
            cp.pixels[2] = (0,0,255)
            cp.pixels[3] = (0,0,255)
            cp.pixels[4] = (0,0,255)
            cp.pixels[5] = (0,0,255)
            cp.pixels[6] = (0,0,0)
            cp.pixels[7] = (0,0,0)
            cp.pixels[8] = (0,0,0)
            cp.pixels[9] = (0,0,0)
           
        if diceroll == 7:
            cp.pixels[0] = (0,0,255)
            cp.pixels[1] = (0,0,255)
            cp.pixels[2] = (0,0,255)
            cp.pixels[3] = (0,0,255)
            cp.pixels[4] = (0,0,255)
            cp.pixels[5] = (0,0,255)
            cp.pixels[6] = (0,0,255)
            cp.pixels[7] = (0,0,0)
            cp.pixels[8] = (0,0,0)
            cp.pixels[9] = (0,0,0)
            
        if diceroll == 8:
            cp.pixels[0] = (0,0,255)
            cp.pixels[1] = (0,0,255)
            cp.pixels[2] = (0,0,255)
            cp.pixels[3] = (0,0,255)
            cp.pixels[4] = (0,0,255)
            cp.pixels[5] = (0,0,255)
            cp.pixels[6] = (0,0,255)
            cp.pixels[7] = (0,0,255)
            cp.pixels[8] = (0,0,0)
            cp.pixels[9] = (0,0,0)
           
        if diceroll == 9:
            cp.pixels[0] = (0,0,255)
            cp.pixels[1] = (0,0,255)
            cp.pixels[2] = (0,0,255)
            cp.pixels[3] = (0,0,255)
            cp.pixels[4] = (0,0,255)
            cp.pixels[5] = (0,0,255)
            cp.pixels[6] = (0,0,255)
            cp.pixels[7] = (0,0,255)
            cp.pixels[8] = (0,0,255)
            cp.pixels[9] = (0,0,0)
            
        if diceroll == 10:
            cp.pixels[0] = (0,0,255)
            cp.pixels[1] = (0,0,255)
            cp.pixels[2] = (0,0,255)
            cp.pixels[3] = (0,0,255)
            cp.pixels[4] = (0,0,255)
            cp.pixels[5] = (0,0,255)
            cp.pixels[6] = (0,0,255)
            cp.pixels[7] = (0,0,255)
            cp.pixels[8] = (0,0,255)
            cp.pixels[9] = (0,0,255)
          
            
    if cp.button_b:
        cp.pixels.fill((0,0,0))