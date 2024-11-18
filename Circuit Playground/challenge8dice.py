from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run
import time     #Import time for program to be able to run on time durations

cp.pixels.brightness = 0.1      #Turning brightness down


while True:		#Has program run all the time
    import random       #Importing random to get random integers
    diceroll = random.randint(1,11)     #Creating variable for dice roll that can be 1-10
    if cp.button_a:     #Showing what happens if button a is pressed
        if diceroll == 1:       #Showing what happens if dice roll is one
            cp.pixels[0] = (0,0,255)        #Pixel 0 is blue
            cp.pixels[1] = (0,0,0)      #Pixel 1 is off
            cp.pixels[2] = (0,0,0)      #Pixel 2 is off
            cp.pixels[3] = (0,0,0)      #Pixel 3 is off
            cp.pixels[4] = (0,0,0)      #Pixel 5 is off
            cp.pixels[5] = (0,0,0)      #Pixel 6 is off
            cp.pixels[6] = (0,0,0)      #Pixel 7 is off
            cp.pixels[7] = (0,0,0)      #Pixel 8 is off
            cp.pixels[8] = (0,0,0)      #Pixel 9 is off
            cp.pixels[9] = (0,0,0)      #Pixel 10 is off
           
           


        if diceroll == 2:       #Showing what happens if dice roll is two
            cp.pixels[0] = (0,0,255)        #Pixel 0 is blue
            cp.pixels[1] = (0,0,255)        #Pixel 1 is blue
            cp.pixels[2] = (0,0,0)      #Pixel 2 is off
            cp.pixels[3] = (0,0,0)      #Pixel 3 is off
            cp.pixels[4] = (0,0,0)      #Pixel 4 is off
            cp.pixels[5] = (0,0,0)      #Pixel 5 is off
            cp.pixels[6] = (0,0,0)      #Pixel 6 is off
            cp.pixels[7] = (0,0,0)      #Pixel 7 is off
            cp.pixels[8] = (0,0,0)      #Pixel 8 is off
            cp.pixels[9] = (0,0,0)      #Pixel 9 is off
           
        if diceroll == 3:       #Showing what happens if dice roll is three
            cp.pixels[0] = (0,0,255)        #Pixel 0 is blue
            cp.pixels[1] = (0,0,255)        #Pixel 1 is blue
            cp.pixels[2] = (0,0,255)        #Pixel 2 is blue
            cp.pixels[3] = (0,0,0)      #Pixel 3 is off
            cp.pixels[4] = (0,0,0)      #Pixel 4 is off
            cp.pixels[5] = (0,0,0)      #Pixel 5 is off
            cp.pixels[6] = (0,0,0)      #Pixel 6 is off
            cp.pixels[7] = (0,0,0)      #Pixel 7 is off
            cp.pixels[8] = (0,0,0)      #Pixel 8 is off
            cp.pixels[9] = (0,0,0)      #Pixel 9 is off
           
        if diceroll == 4:       #Showing what happens if dice roll is four
            cp.pixels[0] = (0,0,255)        #Pixel 0 is blue
            cp.pixels[1] = (0,0,255)        #Pixel 1 is blue
            cp.pixels[2] = (0,0,255)        #Pixel 2 is blue
            cp.pixels[3] = (0,0,255)        #Pixel 3 is blue
            cp.pixels[4] = (0,0,0)      #Pixel 4 is off
            cp.pixels[5] = (0,0,0)      #Pixel 5 is off
            cp.pixels[6] = (0,0,0)      #Pixel 6 is off
            cp.pixels[7] = (0,0,0)      #Pixel 7 is off
            cp.pixels[8] = (0,0,0)      #Pixel 8 is off
            cp.pixels[9] = (0,0,0)      #Pixel 9 is off
         
        if diceroll == 5:       #Showing what happens if dice roll is five
            cp.pixels[0] = (0,0,255)        #Pixel 0 is blue
            cp.pixels[1] = (0,0,255)        #Pixel 1 is blue
            cp.pixels[2] = (0,0,255)        #Pixel 2 is blue
            cp.pixels[3] = (0,0,255)        #Pixel 3 is blue
            cp.pixels[4] = (0,0,255)        #Pixel 4 is blue
            cp.pixels[5] = (0,0,0)      #Pixel 5 is off
            cp.pixels[6] = (0,0,0)      #Pixel 6 is off
            cp.pixels[7] = (0,0,0)      #Pixel 7 is off
            cp.pixels[8] = (0,0,0)      #Pixel 8 is off
            cp.pixels[9] = (0,0,0)      #Pixel 9 is off
           
        if diceroll == 6:       #Showing what happens if dice roll is six
            cp.pixels[0] = (0,0,255)        #Pixel 0 is blue
            cp.pixels[1] = (0,0,255)        #Pixel 1 is blue
            cp.pixels[2] = (0,0,255)        #Pixel 2 is blue
            cp.pixels[3] = (0,0,255)        #Pixel 3 is blue
            cp.pixels[4] = (0,0,255)        #Pixel 4 is blue
            cp.pixels[5] = (0,0,255)        #Pixel 5 is blue
            cp.pixels[6] = (0,0,0)      #Pixel 6 is off
            cp.pixels[7] = (0,0,0)      #Pixel 7 is off
            cp.pixels[8] = (0,0,0)      #Pixel 8 is off
            cp.pixels[9] = (0,0,0)      #Pixel 9 is off
           
        if diceroll == 7:       #Showing what happens if dice roll is seven
            cp.pixels[0] = (0,0,255)        #Pixel 0 is blue
            cp.pixels[1] = (0,0,255)        #Pixel 1 is blue
            cp.pixels[2] = (0,0,255)        #Pixel 2 is blue
            cp.pixels[3] = (0,0,255)        #Pixel 3 is blue
            cp.pixels[4] = (0,0,255)        #Pixel 4 is blue
            cp.pixels[5] = (0,0,255)        #Pixel 5 is blue
            cp.pixels[6] = (0,0,255)        #Pixel 6 is blue
            cp.pixels[7] = (0,0,0)      #Pixel 7 is off
            cp.pixels[8] = (0,0,0)      #Pixel 8 is off
            cp.pixels[9] = (0,0,0)      #Pixel 9 is off
           
        if diceroll == 8:       #Showing what happens if dice roll is eight
            cp.pixels[0] = (0,0,255)        #Pixel 0 is blue
            cp.pixels[1] = (0,0,255)        #Pixel 1 is blue
            cp.pixels[2] = (0,0,255)        #Pixel 2 is blue
            cp.pixels[3] = (0,0,255)        #Pixel 3 is blue
            cp.pixels[4] = (0,0,255)        #Pixel 4 is blue
            cp.pixels[5] = (0,0,255)        #Pixel 5 is blue
            cp.pixels[6] = (0,0,255)        #Pixel 6 is blue
            cp.pixels[7] = (0,0,255)        #Pixel 7 is blue
            cp.pixels[8] = (0,0,0)      #Pixel 8 is off
            cp.pixels[9] = (0,0,0)      #Pixel 9 is off
           
        if diceroll == 9:       #Showing what happens if dice roll is nine
            cp.pixels[0] = (0,0,255)        #Pixel 0 is blue
            cp.pixels[1] = (0,0,255)        #Pixel 1 is blue
            cp.pixels[2] = (0,0,255)        #Pixel 2 is blue
            cp.pixels[3] = (0,0,255)        #Pixel 3 is blue
            cp.pixels[4] = (0,0,255)        #Pixel 4 is blue
            cp.pixels[5] = (0,0,255)        #Pixel 5 is blue
            cp.pixels[6] = (0,0,255)        #Pixel 6 is blue
            cp.pixels[7] = (0,0,255)        #Pixel 7 is blue
            cp.pixels[8] = (0,0,255)        #Pixel 8 is blue
            cp.pixels[9] = (0,0,0)      #Pixel 9 is off
           
        if diceroll == 10:      #Showing what happens if dice roll is ten
            cp.pixels[0] = (0,0,255)        #Pixel 0 is blue
            cp.pixels[1] = (0,0,255)        #Pixel 1 is blue
            cp.pixels[2] = (0,0,255)        #Pixel 2 is blue
            cp.pixels[3] = (0,0,255)        #Pixel 3 is blue
            cp.pixels[4] = (0,0,255)        #Pixel 4 is blue
            cp.pixels[5] = (0,0,255)        #Pixel 5 is blue
            cp.pixels[6] = (0,0,255)        #Pixel 6 is blue
            cp.pixels[7] = (0,0,255)        #Pixel 7 is blue
            cp.pixels[8] = (0,0,255)        #Pixel 8 is blue
            cp.pixels[9] = (0,0,255)        #Pixel 9 is blue
         
           
    if cp.button_b:     #Showing what happens if button b is pushed
        cp.pixels.fill((0,0,0))     #Turning all lights off

       


