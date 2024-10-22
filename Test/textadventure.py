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
        enter_darkforest()      #Sending user back to function enter_darkforest to try again

def enter_hut ():       #Defining function of entering hut
    print("You entered the hut and walk into the kitchen. You see an old lady and start talking to her. She offers you 2 candies. One will not kill you and she will give you food and warm clothing for the rest of the adventure but one will kill you instantly.")   #Describing scene to users so they can make a choice 
    print("You have a 50 percent chance of getting either one. Do you:")        #Explaining to users they will have a 50% randomized choice between 2 candies or can exit safely
    print("1. Take the risk and choose between the 2 candies")      #Giving users 1st option of choosing between candies
    print("2. Turn down the old lady and walk back outside.")       #Giving user 2nd option to exit hut safely
    choice3 = input("> ")       #Place for users to enter their choice of 1 or 2
    if choice3 == "1":          #Showing what happens if user enters 1
        print("You have randomly selected a candy and the results are...")  #Intro to what will happen to them
        import random       #Calling random into function for options
        r = random.randrange(0,2)   #Having a random function to choose between 0 and 1
        if r == 0:                  #Stating what happens if random number = 0
            print("Congrats you have selected the right candy and have now earned food and warm clothing for the adventure!")   #Printing what happens because they choose the right candy and get supplies
            exit_housesafely ()    #Sending users to go back outside function into forest safely
        else:       #Stating what happens if the random number does not equal zero
            print("Sadly, you chose the wrong candy and died. GAME OVER")   #Printing their final destiny of their death and that the game is now over
    elif choice3 == "2":      #Showing what happens if user enters 2
        print("You safely exit the house but without food and warm clothes")    #Prining what happens when they choose to just go back outside
        exit_housesafely ()      #Sending users to the function of exiting the house safely 
    else:       #Showing what happens if users response is invalid
        print("Invalid choice. Try again and please enter 1 or 2.") #Telling user to enter a valid number
        enter_hut ()        #Sending user back to enter hut function to try again

def continue_walking ():   
    print("You continue walking")

def exit_housesafely ():  #NEED TO FINISH LATER, THE ABOVE FUNCTION ALL LEADS TO THIS 
    print("Exited house safely")


def enter_foggyfield ():        #Defining function of entering the foggy field
    print("You entered the foggy field and after walking for awhile you see a murky lake. You are not sure what is in it. Do you: ")   #Setting up scene for users to make the right choice on how to cross lake 
    print("1. Try to look for supplies to build a raft")        #Giving users 1st option of looking for supplies to build a raft
    print("2. Try to find a way around lake by walking")        #Giving users 2nd option of walking around lake
    print("3. Try to swim across lake as it doesn't seem too far")  #Giving users 3rd option to try and swim across lake
    choice4 = input("> ")       #Place for users to enter their selected choice
    if choice4 == "1":      #Showing what happens if user enters 1
        print("You find some driftwood and rope left nearby to build a raft. Your raft safely makes it across the lake.")   #Printing description of what happened to them when they searched for materials
        across_lake ()      #Sending user to across lake function because they have safely crossed
    elif choice4 == "2":    #Showing what happens if user enters 2
        print("You walk about a half a mile to the left and see a bridge and safely cross it to the other side of the lake.")   #Printing description of what happened to them when they tryed to walked around lake
        across_lake ()  #Sending user to across lake function because they safely crossed
    elif choice4 == "3":    #Showing what happens if user enters 3
        print("You try to swim across the river and your leg gets bit by a shark. You barely make it back to shore and are forced to scream for help.") #Printing description of what happend to them when they tryed to cross lake by swimming
        help_needed ()  #Sending user to help needed function because they are bleeding
    else:               #Showing what happens is users response is invalid
        print("Invalid choice. Try again and please enter 1,2, or 3")   #Telling user they need to enter a 1, 2, or 3 to get a valid response
        enter_foggyfield () #Sending user back to enter foggy field function to try again
    
    

def continue_walking ():
    print("You continue walking")

def across_lake ():
    print("You are across lake safely")

def help_needed ():
    print("You scream for help and a young women finds you bleeding out")


start_adventure ()               #Calling function to start entire adventure
