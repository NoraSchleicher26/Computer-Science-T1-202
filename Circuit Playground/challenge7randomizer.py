from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run
import time     #Import time for program to be able to run on time durations



while True:     #Has program run all the time
    import random       #Importing random so we can get random integers for colors
    x, y, z = cp.acceleration       #Getting acceleration involved 
    shake_threshold = 9.0      #Setting shake threshold that will start program
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:        #If statement for if shake threshold is less than the shake
        cp.pixels[0] = (random.randint(1,256), random.randint(1,256), random.randint(1,256))        #Setting light 0 to random color with randint
        cp.pixels[1] = (random.randint(1,256), random.randint(1,256), random.randint(1,256))        #Setting light 1 to random color with randint
        cp.pixels[2] = (random.randint(1,256), random.randint(1,256), random.randint(1,256))        #Setting light 2 to random color with randint
        cp.pixels[3] = (random.randint(1,256), random.randint(1,256), random.randint(1,256))        #Setting light 3 to random color with randint
        cp.pixels[4] = (random.randint(1,256), random.randint(1,256), random.randint(1,256))        #Setting light 4 to random color with randint
        cp.pixels[5] = (random.randint(1,256), random.randint(1,256), random.randint(1,256))        #Setting light 5 to random color with randint
        cp.pixels[6] = (random.randint(1,256), random.randint(1,256), random.randint(1,256))        #Setting light 6 to random color with randint
        cp.pixels[7] = (random.randint(1,256), random.randint(1,256), random.randint(1,256))        #Setting light 7 to random color with randint
        cp.pixels[8] = (random.randint(1,256), random.randint(1,256), random.randint(1,256))        #Setting light 8 to random color with randint
        cp.pixels[9] = (random.randint(1,256), random.randint(1,256), random.randint(1,256))        #Setting light 9 to random color with randint