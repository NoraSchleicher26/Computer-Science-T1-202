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

def continue_walking ():        #Defining function of continue walking for user
    print("You continue walking and spot a mysterious man offering you shelter and food if you come with him. Do you:")     #Showing description of scenario so user can make the "right" choice
    print("1. Follow man to his house for the shelter and food he talks of")        #Giving user 1st option of going to mysterious man's house
    print("2. Politely decline and walk away")      #Giving user 2nd option of walking away from man
    choice5 = input("> ")       #Place for user to enter their choice of 1 or 2
    if choice5 == "1":      #Showing what happens if user enters 1
        print("After following man to his house, he leads you to his basement filled with food but as he heads up the stairs, he locks the door and says, You will stay here forever with me. Adventure is now over")     #Printing decription of what has happened to user and their adventure is now over
    elif choice5 == "2":        #Showing what happens if user enters 2
        print("You narrowly avoid a kidnapping and are able to continue walking hopefully towards freedom")     #Printing description of what happens when user chooses to walk away
        freedom_choice()        #Sending user to function freedom choice
    else:       #Showing what happens if user enters invalid response
        print("Invalid choice. Try again and please enter 1 or 2.") #Telling user to enter a valid number
        continue_walking ()     #Sending user back to continue walking function to try again

def freedom_choice():   #Defining function of freedom choice
    print("You escaped the man and now see the trail split once again. To the left is a greenish haze and to the right is a pinkish haze. Do you:")     #Setting up scene for users to make their best choice
    print("1. Go to the left towards the greenish haze")    #Giving user option 1 of going into green haze
    print("2. Go to the right towards the pinkish haze")    #Giving user option 2 of going into pink haze
    choice6 = input("> ")       #Place for users to enter their choice of 1 or 2
    if choice6 == "1":      #Showing what happens if user enters 1
        print("As you enter the green haze you start to feel very sleepy and realize the haze will cause you to fall into a forever deep sleep unless someone could find and save you and you collapse to the floor. Adventure is now over.")   #Printing summary of what happened to user and what their fate is now and that their adventure is now over
    elif choice6 == "2":    #Showing what happens if user enters 2
        print("As you make your way through the pink haze you start to see natural sunlight and spot your old house. You run home to your parents and are now safe.")   #Printing what happens to user when they walk into pink and that they are now safe
    else:   #Showing what happens if users response is invalid
        print("Invalid choice. Try again and please enter 1 or 2.") #Telling user to enter a valid number
        freedom_choice ()       #Sending user back to freedom choice function to try again

def exit_housesafely():     #Defining function of exit house safely
    print("You exited house safely  with food and warm clothes. A purple monster approaches you and asks for some food. Do you:") #Printing scenario for user to make best choice based on situation
    print("1. Give monster some of your food")  #Giving user option 1 of giving monster food
    print("2. Don't give monster food") #Giving user option 2 of not giving monester food
    choice7 = input ("> ")  #Place for user to enter response of 1 or 2
    if choice7 == "1":  #Showing what happens if user enters 1
        print("Monster graciously accepts food and offers to show you way out of forest for your kindness. He leads you down a path and soon you are able to exit the forest into the normal world again. You are safe.") #Printing what happens after user gives monster food and that they are now safe because of their kindness
    elif choice7 == ("2"):  #showing what happens if user enters 2
        print("Monster understands and walks away leaving you alone.")  #Printing what happens and that user is now alone
        left_alone () #Sending user to function left alone beause of their choice
    else:
        print("Invalid choice. Try again and please enter 1 or 2.") #Telling user to enter a valid number
        exit_housesafely ()     #Sending user back to exit house safely function to try again


def left_alone():   #Defining function of left alone
    print("Once left alone, you see underground trail with a DO NOT ENTER SIGN but you are desperate to get out as you are running out of food. Do you:") #Printing description of scenario for users to understand what is happening
    print("1. Enter underground trail") #Giving user option 1 of entering trail
    print("2. Don't enter trail and sit on a rock waiting for someone to help you")     #Giving user option 2 of not entering trail and waiting
    choice8 = input("> ")   #Place for user to enter choice of 1 or 2
    if choice8 == "1":  #showing what happens if user enters 1
        print("You walk cautiously through trail and eventually see light, you walk outside the trail and see the beach. You are now safely in Florida!") #Telling user what happens to them when they go to underground trail and that they are now safe
    elif choice8 == "2":    #Showing user what happens if user enters 2
        print("After running out of food you start to starve and eventually die after getting no help. Game is now over")   #Telling user wha happens after they run of out food and that their game is now over
    else:       #Showing what happens if users response is invalid
        print("Invalid choice. Try again and please enter 1 or 2.") #Telling user to enter a valid number
        left_alone ()       #Sending user back to left alone function to try again

    


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
        print("You try to swim across the river and your leg gets bit by a shark. You barely make it to the shore and are forced to scream for help.") #Printing description of what happend to them when they tryed to cross lake by swimming
        help_needed ()  #Sending user to help needed function because they are bleeding
    else:               #Showing what happens is users response is invalid
        print("Invalid choice. Try again and please enter 1,2, or 3")   #Telling user they need to enter a 1, 2, or 3 to get a valid response
        enter_foggyfield () #Sending user back to enter foggy field function to try again
    
def across_lake ():     #Defining function of across lake
    print("You are across lake safely and see an old mansion standing tall. You are desperate for food. Do you:")        #Telling user situation they are in after crossing the lake safely
    print("1. Enter the mansion looking for food")  #Giving users 1st option of entering mansion
    print("2. Continue on your path looking for other things to eat")   #Giving users 2nd option of not entering mansion and continuing
    choice9 = input("> ") #Place for users to enter their choice of 1 or 2
    if choice9 == "1": #Showing what happens if user enters 1
        print("You enter and see two flights of stairs one going up and the other going down.") #Telling user what they see after enterig mansion\
        choice_stairs() #Sending user to choice stairs function as a result of their choice
    elif choice9 == "2":    #Showing what happens if user enters 2
        print("You continue walking through path and spot a rock wall.")    #Telling user what happens as they continue through path
        rock_wall ()    #Sending user to rock wall function because of their choice
    else:       #Showing what happens if users response is  invalid
        print("Invalid choice. Try again and please enter 1 or 2.")     #Telling user to enter a valid number
        across_lake ()      #Sending user back to across lake function to try again
      
        
    
def choice_stairs():        #Defining function of choice stairs
    print("You can either go up or down a set of stairs to try and find food/help. Do you:")    #Telling user hwat is going on and the choice they have to make
    print("1. Go downstairs")   #Giving user option 1 of going downstairs
    print("2. Go upstairs") #Giving user option 2 of going upstairs
    choice10 = input("> ")  #Place for users to enter answer of 1 or 2
    if choice10 == "1": #Showing what happens if user enters 1
        print("You go downstairs and see a vampire with 3 boxes staring intently at you.")   #Telling user what happens when they go downstairs and explaining situation
        vampire_boxes ()    #Sending user to function of vampire boxes
    elif choice10 == "2":   #Showing what happens if user enters 2
        print("You start heading up the stairs")   #Telling user what happens when they go  upstairs and see a maze
        maze_choice ()      #Sending user to maze choice function as result of their previous choice
    else:       #Showing what happens when users response is invalid
        print("Invalid choice. Try again and please enter 1 or 2.")     #Telling user to enter a valid number
        choice_stairs ()        #Sending user back to choice stairs function to try again

    

def rock_wall ():   #Defining function of rock wall
    print("The rock wall looms over you and you can't see anyway around it, there is a ladder and a rope both reaching the top and you can only choose to take 1. Do you:")     #Describing situation to user so they can make their choice
    print("1. Try to use the ladder leaning against the wall to reach top")   #Giving user 1st option of using ladder
    print("2. Try to climb the rope up to the top of the wall") #Giving user 2nd option of climbing rope to top
    choice11 = input("> ")      #Place for user to enter response
    if choice11 == "1":         #Showing what happens if user enters 1
        print("As you are climbing to the top, you reach a broken step, but not noticing it, you step on it and fall to your death... Game Over")       #Describing to user what happens when they try to climb the ladder and that there game is now over
    elif choice11 == "2":       #Showing what happens if user enters 2
        print("The rope is able to hold up as you climb the wall and when you reach the top you see the bright blue sky and you feel relief as you realize you are now free from the dark forest. Adventure is over and you are safe.")         #Describing to user what happens when they climb rope and that they are now safe out in the bright blue sky
    else:       #Showing what happens if users response is invalid
        print("Invalid choice. Try again and please enter 1 or 2.")         #Telling user to enter a valid number
        rock_wall ()    #Sending user back to rock wall function to try again

def help_needed (): #Defining function of help needed
    print("You scream for help and a young women finds you bleeding out. She offers to give you a mysterious looking purple medicine to instantly heal you. Do you:")   #Describing situation to user so they can make their own logical choice
    print("1. Accept medicine and drink it")       #Giving user 1st option of taking and drinking medicine
    print("2. Decline medicine and walk away")  #Giving user 2nd option of declining medication and leaving
    choice12 = input("> ")  #Place for users to enter their choice
    if choice12 == "1":     #Showing what happens if user enters 1
        print("The medication heals your leg very quickly and you are able to continue down the path")  #Telling user what happens when they accept medication 
        across_lake () #Sending user to the across lake function because they are now healed enough to continue
    elif choice12 == "2":   #Showing what happens if user enters 2
        print("You thought you were strong enough to continue but the blood loss causes you to faint and eventually leads to your slow and painful death stranded on the shore. You died and adventure is now over.")   #Telling user what happens when they decline medication they needed and that they have died causing adeventure to end
    else:       #Showing what happens when users response is invalid
        print("Invalid choice. Try again and please enter 1 or 2.")         #Telling user to enter a valid number
        help_needed ()  #Sending user back to help needed function to try again


def vampire_boxes():    #Defining function of vamprire boxes
    print("Their is a door behind the vampire that is locked. He tells you that 1 of the 3 boxes has a key that unlocks the door to a new life and freedom but the other 2 have a black essence that will make you forever stay with the vampire so he can suck your blood. Do you:")   #Desrcibing situation to user so they can make a logical choice
    print("1. Accept risk and randomly select a box")
    print("2. Decline risk and go upstairs to the upper part of the home")
    choice13 = input("> ")  #Place for user to enter their choice
    if choice13 == "1":    #Showing what happens if user enters 1
        print("You selected a random box and there is...")  #Setting up intro to results of box
        import random   #Importing random to work for a function needing a random number
        k = random.randrange(0,3)    #Having a random function to choose between 0,1, and 2
        if k == 0:  #Showing what happens if random number is 0
            print ("A key inside! You unlock door and enter an apartment in London. You can now start a new life and your adventure is now safely over")     #Printing description of what happens if randomly selcted box has key and what their life will now be like
        else:   #Showing what happens if random number is not 0
            print ("Nothing in the box. You are now forever trapped with the blood sucking vampire. Adventure is over.")    #Describing to user what happens if they get nothing in box and their final fate with the vampire now
    elif choice13 == "2":   #Showing what happens if user enters 2
        print("You declined the vampire's offer and head to the upstairs of the house.")    #Printing description of what happens if user declines vampire offer
        maze_choice ()      #Sending user to maze choice function as a result of their previous choice
    else:       #Showing what happens if users reponses is invalid
        print("Invalid choice. Try again and please enter 1 or 2.")        #Telling user to enter a valid number
        vampire_boxes ()    #Sending user back to vampire boxes function to try again

def maze_choice():      #Defining function of maze choice
    print("When you go upstairs you see there is a maze with a sign telling you there is a great reward at the end. Do you:")
    print("1. Head out of the house not wanting to do the maze")    #Giving user option 1 of leaving the house
    print("2. Enter maze")  #Giving user 2nd option of entering the maze
    choice14 = input("> ")  #Place for users to enter their choice
    if choice 


start_adventure ()               #Calling function to start entire adventure
