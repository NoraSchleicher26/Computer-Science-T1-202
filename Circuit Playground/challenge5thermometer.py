from adafruit_circuitplayground import cp       #Importing cp for program to run






while True:     #Having program run all the time
    temp_f = cp.temperature     #Creating variable for temperature in Fahrenheit
    temp_c = (temp_f * 9 / 5) + 32      #Converting temperature in Fahrenheit to Celcius
   
   
    if temp_c  > 0:     #Showing what happens if temp_c > 0
        cp.pixels[0] = (0 ,0 ,1)        #Sets light to Blue
    if temp_c > 78:     #Showing what happens if temp_c > 78
        cp.pixels[1] = (0 ,0 ,1)        #Sets light to Blue

    if temp_c > 79:     #Showing what happens if temp_c > 79
        cp.pixels[2] = (0 ,0 ,1)        #Sets light to Blue

    if temp_c > 80:     #Showing what happens if temp_c > 80
        cp.pixels[3] = (1 ,1 ,0)        #Sets light to Yellow

    if temp_c > 81:     #Showing what happens if temp_c > 81
        cp.pixels[4] = (1, 1 ,0)        #Sets light to Yellow

    if temp_c > 82:     #Showing what happens if temp_c > 82
        cp.pixels[5] = (1 ,1 ,0)        #Sets light to Yellow

    if temp_c > 83:     #Showing what happens if temp_c > 83
        cp.pixels[6] = (1 ,1 ,0)        #Sets light to Yellow

    if temp_c > 84:     #Showing what happens if temp_c > 84
        cp.pixels[7] = (1 ,0 ,0)        #Sets light to Red

    if temp_c > 85:     #Showing what happens if temp_c > 85
        cp.pixels[8] = (1 ,0 ,0)        #Sets light to Red

    if temp_c > 86:     #Showing what happens if temp_c > 86
        cp.pixels[9] = (1 ,0 ,0)        #Sets light to Red





        