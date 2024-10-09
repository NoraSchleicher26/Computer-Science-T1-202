x = 0

if x > 0:   # > < == >= <= !=
    print("x is a positive number!")

elif x < 0: #elif statements are always paired to an if
    print("x is a negative number!")
else:       #else statemets are always paired to an if statement
            #else statements never take a condition
            #takes whatever didn't get caught by if statement
    print("x is zero")    

color = input("What color is the light?\n>")

if color.lower() == "green":    #Only one IF
    print("GO")
elif color.lower() == "red":    #No limit to how many elifs you can use
    print("STOP")
elif color.lower() == "yellow":
    print("STOP IF YOU CAN DO SO SAFELY")
else:                           #Only one ELSE
    print("CALL THE POLICE")

#Why do I even need elif statements???
#Can't I just use more if's?
    
x = 10

if x > 5:
    print("x is greater than five")
if x > 8:
    print("x is gretaer than eight")

 ########################

if x > 5:
    print("x is greater than five")
elif x > 8:
    print("x is greater than eight")

#Coin Sorter Analogy:
#Quarters: If
#Nickels, Pennies, and Dimes: Elifs
#Everything Else: else