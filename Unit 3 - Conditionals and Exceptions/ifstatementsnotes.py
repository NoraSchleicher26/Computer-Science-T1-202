#If statements evaluate boolean expressions
#Make decisions abut which code to run next

#Take a temperature
#Print "<temperature> is hot" if the temperature is >= 80
#otherwise, print "<temperature> is not hot"
temperature = input("What is the temperature?\n-")
temperature = int(temperature)
#if, boolean expression, :
#Sort of like a function, no parenthesis!
if temperature >= 80: #If the bool evalutes to True, go inside
    print("The temperature is " + str(temperature) + " degrees.")
    print(str(temperature) + " degrees is hot.")

else: #Else takes NO condition and runs when the if above is false
    #Otherwise...
    print("The temperature is " + str(temperature) + " degrees.")
    print(str(temperature) + " degrees is not hot.")

#Complete the activity-
    #Create a program that asks for a password
    #print "ACCESS GRANTED" if the password is correct
    #print "ACCESS DENIED" if the password is wrong
    #the password is skibidi68

real_password = "skibidi68"
password = input ("What is the password?\n-")

if password == real_password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

#Activity 2, electrical boogaloo
#Create a 5 question quix that prints your score at the end
#Choose any five questions
#EZ

print ("Random quiz:")
real_answer1 = "blue"
answer1 = input("What color is the sky?\n-")
if answer1 == real_answer1:
    print("CORRECT")
    x = 1
else:
    print("WRONG")
    x = 0
real_answer2 = "green"
answer2 = input ("What color is the grass?\n-")
if answer2 == real_answer2:
    print("CORRECT")
    y = 1
else:
    print("WRONG")
    y = 0
real_answer3 = "red"
answer3 = input("What color is a stop sign?\n-")
if answer3 == real_answer3:
    print("CORRECT")
    z = 1
else:
    print("WRONG")
    z =0
real_answer4 = "yellow"
answer4 = input("What color is a banana?\n-")
if answer4 == real_answer4:
    print("CORRECT")
    a = 1
else:
    print ("WRONG")
    a = 0
real_answer5 = "white"
answer5 = input ("What color are clouds?\n-")
if answer5 == real_answer5:
    print("CORRECT")
    b = 1
else:
    print("WRONG")
    b = 0
print("Score:")
print (x + y + z + a + b)



