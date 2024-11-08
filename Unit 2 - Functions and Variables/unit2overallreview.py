#2functions
print("Hello, World!")      #"Hello, World!" is the parameter
input("Please enter your username\n-")  # \n is called an escape character
# \n starts a new line (linebreak)
#input is never required


#Variables
#Syntax-grammar or way you write it
# name = value
x = 5

#Snake naming convenetion - all lowercase, underscore for spaces
#CONCISE: Short and descriptive
username = "schleicher"     #Define string ("string" of characters)
fav_animal = "giraffe"      #Define string ("string" of characters)
total_poptarts = 12         #Define integer (whole number)
percent_complete = 23.52    #Define flaat (decimal number)
is_cool = True              #Define Boolean (True/False)
first_letter = 'c'          #Define Character (single symbol)

total_poptarts = 8          #Reassign, taking existing variable and changing value

#Arithmetic Operators
#   +   -   *   /   **  %    //
print(4 + 4) # = 8
print("4" + "4") # = 44
print("cat" + "dog") # = catdog
print("cat" * 3) # = catcatcat
print("cat" + 3) # = ERROR: Cannot use + for string and int

#Make some working programs
#1. add two numbers using input
x = input("What is x?\n-")      #input() always returns a string
x = int(x)                      #converting from string to integer 
y = input ("What is y?\n-")     #even if you type in a number
y = int(y)                      #converting from string to integer
print(x + y)

#2. Converts celcius to farenheit
temp_celcius = input("What is the temperature in Celcius?\n-")
temp_celcius = int(temp_celcius)    #converting string to integer
temp_farenheit = (temp_celcius * 1.8) + 32
print(temp_celcius + " degrees C equals " + temp_farenheit + " degrees F")



#Some conversion functions
str()
int()
float()
bin()
bool()

#The stuff that goes between the parenthesis is called PARAMETERS
#Parameters are the values that the function needs to run

#Functions
#Functions are a lot like variables
#They have names
#They can be recalled from memory by calling their name
#They store information
#Variables store values, functions store code

def potato():       #Defining keyword + name + () + :
    print("potato") #Lines indented underneath are "inside" the function

#functions are not ran when they are defined
#they must be called by their name to run
potato ()       #Every function call needs open and closed parenthesis
                #Even if it has no parameters

def jump(how_high):     #Using paramteter in function
    print("You jumped " + str(how_high) + " inches!")

jump(14)        #Need the 14 or else function won't work because function calls for one parameter

def make_a_word(a, b, c, d, e, f, g, h, i, j, k):       #Using 11 parameters
    print(a + b + c + d + e + f + g + h + i + j + k)

make_a_word("Z", "a", "c", "k", "O", "s", "o", "w", "s", "k", "i") # a = Z, need 11 for parameters

#Functions can have many many lines
def top_five_games():
    print("1. Elden Ring'")
    print("2. Shadow of the Clossus")
    print("3. Minecraft")
    print("4. Diablo 3")
    print("5. Overwatch")

#Scope: Global and local Variables!!
#Scope refers to the context in which the variable was defined
#Global- defined at no indentation level
#local- defined inside of a function

#Global variables can be used anywhere
todd = "cool guy"       #Global Variable- no indentation level

#Local variables only exist in the scope they were defined
def my_function ():
    smother = "not cool guy"        #Local Variable- define in a function
    todd = "strange guy"            #local variable even though it has the same name
    print(todd)                     #prints the local variable todd. prints "strange guy"
    #When you call a variable in a function
    #It searches Local Variables first, then global variables

#If you want to reassign a global variable inside of a function
    todd = "cool guy"
def my_function2():
    global todd             #In this function, whenever I call todd
                            #I mean the global todd, not the local
    todd = "strange guy"    #Reassign todd - global
    print (todd)            #Print todd - global

#Return functions
    #Functions can also return values
    #The value that is returned is sent back to where the function was called
    #This is very similar to how a variable works
    #The function does its work and returns an answer back
def add2 (x, y):
    return x + y    #returns the sum of x and y to where the function was called

add2(2, 10) #Does not print anything! We never told it to print

answer = add2(2,10)
print (answer)



