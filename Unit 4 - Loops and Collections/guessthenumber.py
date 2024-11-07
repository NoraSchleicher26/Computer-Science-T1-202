

#Guess the number
import random     
guess = -1
number = random.randint(0, 101)
trys = 0

while guess != number:
    trys += 1

    try:
        guess = int(input("What is your guess?\n>"))
    except:
        print("Hmm... That's not right...")

    if guess > number:
        print("Too large, try again...")
    elif guess < number:
        print("Too small, try again...")
    else: 
        print("Bingo! The correct number was " + str(number))
        print ("It took you " + str(trys) + " trys")

print("Nice job")