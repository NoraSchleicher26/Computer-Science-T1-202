from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run
   
cp.pixels.brightness = 0.01     #Turning brightness down
while True:
    if cp.switch:       #Showing what happens if switch is to the right
        cp.pixels[0] = (0,255,0)        #Pixel zero is green
        cp.pixels[1] = (0,255,0)        #Pixel one is green
        cp.pixels[2] = (0,255,0)        #Pixel two is green
        cp.pixels[3] = (0,255,0)        #Pixel three is green
        cp.pixels[4] = (0,255,0)        #Pixel four is green
        cp.pixels[5] = (0,0,0)      #Pixel five is off
        cp.pixels[6] = (0,0,0)      #Pixel six is off
        cp.pixels[7] = (0,0,0)      #Pixel seven is off
        cp.pixels[8] = (0,0,0)      #Pixel eight is off
        cp.pixels[9] = (0,0,0)      #Pixel nine is off


    else:       #Showing what happens if switch is to the left
        cp.pixels[0] = (0,0,0)      #Pixel zero is off
        cp.pixels[1] = (0,0,0)      #Pixel one if off
        cp.pixels[2] = (0,0,0)      #Pixel two is off
        cp.pixels[3] = (0,0,0)      #Pixel three is off
        cp.pixels[4] = (0,0,0)      #Pixel four is off
        cp.pixels[5] = (0,255,0)        #Pixel five is green
        cp.pixels[6] = (0,255,0)        #Pixel six is green
        cp.pixels[7] = (0,255,0)        #Pixel seven is green
        cp.pixels[8] = (0,255,0)        #Pixel eight is green
        cp.pixels[9] = (0,255,0)        #Pixel nine is green
