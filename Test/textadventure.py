def start_adventure ():     #Defining function for starting the adventure
    print("You have come to a trail split. One path is a dark haunting forest, the other is a foggy field. Do you:")        #Describing opening story so users have an idea of situation
    print("1. Go left into the dark haunting forest")       #Giving users 1st option of entering forest
    print("2. Go right into the foggy field")               #Giving users 2nd option of entering field
    choice1 = input("> ")       #Place for users to enter their choice of 1 or 2
    if choice1 == "1":          #Showing what happens if user enters 1
        enter_darkforest ()     #Sending user to function enter_darkforest
    elif choice1 == "2":        #Showing what happens if user enters 2
        enter_foggyfield ()     #Sending user to function enter_foggyfield
    else:                       #Showing what happens if user enters anything besides 1 or 2
        print("Invalid choice. Try again and please enter 1 or 2.")      #Telling user their answer is invalid and they need to enter 1 or 2 to continue
        start_adventure()       #Sending user back to first function to answer correctly
    
def enter_darkforest ():        #Defining function for the option of entering the dark forest
    print("You have entered the dark forest. You spot a little wooden hut with broken windows on the side of the trail. Do you:")       #Describing scene to users so they can make their choice
    print("1. Continue walking down the trail")     #Giving users 1st option to continue walking
    print("2. Enter the wooden hut")                #Giving users 2nd option of entering mysterious hut
    choice2 = input("> ")       #Place for users to enter their choice of 1 or 2
    if choice2 == "1":          #Showing what happens if user enters 1
        continue_walking ()      #Sending user to function continue_walking
    elif choice2 == "2":        #Showing what happens is user enters 2
        enter_hut ()            #Sending user to function enter_hut
    else:                       #Showing what happens if user enters anything besides 1 or 2
        print("Invalid choice. Try again and please enter 1 or 2.")     #Telling user their answer is invalid and they need to enter 1 or 2
        enter_darkforest()      #sending user back to function enter_darkforest to try again
    


def enter_foggyfield ():  
    print("You entered the foggy field. ")      #Defining function for the option of entering the foggy field

def continue_walking ():
    print("You continue walking")
def enter_hut():
    print("You enter hut")

start_adventure ()               #Calling function to start entire adventure
