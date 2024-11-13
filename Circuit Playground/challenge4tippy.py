from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run

cp.pixels.brightness = 0.01     #Turning down brightness of pixels

while True:
    x, y, z = cp.acceleration 
    if x < -5:      #What happens when tilted left
        cp.pixels[0] = (0,0,0)      #Pixel zero is off
        cp.pixels[1] = (0,255,0)        #Pixel one is green
        cp.pixels[2] = (0,255,0)        #Pixel two is green
        cp.pixels[3] = (0,255,0)        #Pixel three is green
        cp.pixels[4] = (0,0,0)      #Pixel four is off
        cp.pixels[5] = (0,0,0)      #Pixel five is  off
        cp.pixels[6] = (0,0,0)      #Pixel six is off
        cp.pixels[7] = (0,0,0)      #Pixel seven is off
        cp.pixels[8] = (0,0,0)      #Pixel eight is off
        cp.pixels[9] = (0,0,0)      #Pixel nine is off
        

    elif x > 5:       #What happens when tilted right
        cp.pixels[0] = (0,0,0)      #Pixel zero is off
        cp.pixels[1] = (0,0,0)      #Pixel one is off
        cp.pixels[2] = (0,0,0)      #Pixel two is off
        cp.pixels[3] = (0,0,0)      #Pixel three is off
        cp.pixels[4] = (0,0,0)      #Pixel four is off
        cp.pixels[5] = (0,0,0)      #Pixel five is off
        cp.pixels[6] = (255,0,0)        #Pixel six is red
        cp.pixels[7] = (255,0,0)        #Pixel seven is red
        cp.pixels[8] = (255,0,0)        #Pixel eight is red
        cp.pixels[9] = (0,0,0)      #Pixel nine is off