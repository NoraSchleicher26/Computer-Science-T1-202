#Loop control statements
#Allow you to change how loops operate
#Do things like quit the loop early. skip the current loop, and even do nothing
# break, continue, and pass


#break
#Exits a loop prematurely, before it was supposed to end


#Example

bag_of_fruits = ["apple", "orange", "bug", "watermelon", "pear"]

for fruit in bag_of_fruits:
    if fruit == "bug":
        print("Uh oh, you found a bug in the bag...")
        break       #the break statement exits the loop immediately and continues
    else:
        print("You ate a " + fruit)


#continue
#Skips the current loop
#It does not exit the entire loop, just moves on to the next iteration
        
orders = [15, 30, 35, 23, 100, 3, 10, 22]

#Only apply discount for orders above 20 dollars
#Coupon applying program
for order in orders:
    if order < 20:
        continue    #Skips the rest of the loop iteration and goes to the next iteration
    print(str(order) + " order discounted 5% to $" + str(order * 0.95))

#pass
#Does nothing
#Usually used as a placeholder while writing code
#Text adventure project
    
if True:
    pass 
def enter_forest():
    pass

def swim_river():
    pass

def eat_icecream():
    pass