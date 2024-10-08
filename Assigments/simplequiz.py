#Create a quiz that asks questions and tallies your score at the end.
#Use input statements to ask questions and store the answers as variables.
#Create a function called 'tally_score' that checks if the answers are corret.
#Use if statements to check answers.
#Input statements outside the function.
#if statements inside the function, no function parameters needed.
score = 0                                                        #Defining score variable
print("Quiz:")                                                   #Printing name of program
real_answer1 = "red"                                             #Creating variable for 1st actual answer
answer1 = input("What color is a stop sign?\n-")                 #Asking user 1st question

real_answer2 = "blue"                                            #Creating variable for 2nd actual answer
answer2 = input("What color is the ocean?\n-")                   #Asking user 2nd question

real_answer3 = "orange"                                          #Creating variable for 3rd actual answer
answer3 = input("What color is a traffic cone?\n-")              #Asking user 3rd question

real_answer4 = "white"                                           #Creating variable for 4th actual answer
answer4 = input("What color are clouds on a sunny day?\n-")      #Asking user 4th question

real_answer5 = "yellow"                                          #Creating variable for 5th actual answer
answer5 = input("What color is a banana?\n-")                    #Asking user 5th question

def tally_score():                                               #Defining function to score quiz correctly
    global score                                                 #Pulling global variable into function
    if answer1 == real_answer1:                                  #Checking answer for question 1
        score = score + 1                                        #Adding one to score if correct

    if answer2 == real_answer2:                                  #Checking answer for question 2
        score = score + 1                                        #Adding one to score if correct

    if answer3 == real_answer3:                                  #Checking answer for question 3
        score = score + 1                                        #Adding one to score if correct
   
    if answer4 == real_answer4:                                  #Checking answer for question 4
        score = score + 1                                        #Adding one to score if correct
   
    if answer5 == real_answer5:                                  #Checking answer for question 5
        score = score + 1                                        #Adding one to score if correct
    
    print("Score:")                                              #Printing "Score:"
    print(score)                                                 #Printing actual added score from quiz

tally_score ()                                                   #Calling function to run