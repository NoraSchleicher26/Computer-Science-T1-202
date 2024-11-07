#There are a couple types of loops in python
#The for loop lets you iterate a list
#-great for looping a set number of times
#BUT WHAT IF we need to loop an uncertain number of time???
#ex. Enterting your password
#You could get it right the first time
#It could take you a million tries
#Or anything in between

#A while loop continues looping until the condition is no longer True
real_pass = "potato45"
entered_pass = ""

attempts = 0

while real_pass != entered_pass:        #Check if the entered password matches the real one
    #Ask for the password
    entered_pass = input("Please enter the password\n>")
    attempts += 1

    #Check if password is correct
    if entered_pass == real_pass:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        print(str(attempts) + " attempts.")
        print("try again...")
        

#End password checking
print("Welcome!")


#Try this
#UPDATE this while loop so that it prints how many attempts you are on
#Print number of attempts every loop

#With while loops, you need to be careful for infinite loops
#When you put your computer in rest mode, it has nightmares about infinite loops/joke
#An infinite loop happens when you enter a while loop that can never be escaped.
#Example (do not click run...)
#while True:            (This is never not true)
        #print("uh oh")

#count = 0
#while True:
#    count += 1
#    print(count)

#print("All done:")

#Real World Example:
# "Type "exit" to quit

user_input = ""

while user_input != "exit":
    user_input = input("Enter something (type 'exit' to quit)\n>")
    print("You entered: " + user_input)

print("All done")
