#1
word1 = input ("Write a random word\n-")         #Asking user for first random word
word2 = input ("Write a second random word\n-")  #Asking user for second random word
word3 = input ("Write a third random word\n-")   #Asking user for third random number
print (word1 + " " + word2 + " " + word3)        #Printing concatenation of users 3 random words

#2
def add_three (x, y, z):    #Defining function of adding 3 integers
    x = int(x)          #Converting x string into an integer
    y = int(y)          #Converting y string into an integer
    z = int(z)          #Converting z string into an integer
    print (x + y + z)   #Printing sum of 3 integers given by user (x, y, z)

x = input ("Write first integer\n-")    #Asking user for first integer
y = input ("Write second integer\n-")   #Asking user for second integer
z = input ("Write third integer\n-")    #Asking user for third integer
add_three (x, y, z)                         #Calling Function to run with 3 given integers

#3
def data_three ():                          #Defining function of adding integer and float and concatenating with a word
    word = input("Write a word\n-")         #Asking user for a word
    integer = input("Write an integer\n-")  #ASking user for an integer
    float_1 = input("Write a float\n-")     #Asking user for a float
    word = str(word)                        #Converting word given into a string
    integer = int(integer)                  #Converting integer given into an integer
    float_1 = float(float_1)                #Converting float given into a float
    add = (integer + float_1)               #Adding integer and float given together
    add = str(add)                          #Converting the added integer and float into a string so it works when printed
    concatenation = (add + " " + word)      #Concatenating integer/float number with word
    print (concatenation)                   #Printing concatenation of added integer float number and word

data_three ()                               #Calling function to run 