#Loop control statements
#Allow you to change how loops operate
#Do things like quit the loop early. skip the current loop, and even do nothing
# break, continue, and pass


#break
#exits a loop prematurely, before it was supposed to end


#Example

bag_of_fruits = ["apple", "orange", "bug", "watermelon", "pear"]

for fruit in bag_of_fruits:
    if fruit == "bug":
        print("Uh oh, you found a bug in the bag...")
        break       #the break statement exits the loop immediately and continues
    else:
        print("You ate a " + fruit)