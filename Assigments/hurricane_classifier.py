print("Hurricane Classifier:")
speed = int(input("What is the wind speed in MPH?\n-"))
if speed < 74:
    print ("Tropical Storm")
elif speed < 96:
    print ("Category One")
elif speed < 111:
    print ("Category Two")
elif speed < 130:
    print ("Category Three")
elif speed < 157:
    print ("Category Four")
else:
    print("Category Five")