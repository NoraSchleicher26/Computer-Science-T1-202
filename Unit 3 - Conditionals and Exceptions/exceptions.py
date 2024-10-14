# Exception Handling
# How programs deal with unexpected errors
# Safety net for when things go wrong
# Write a program that asks for two numbers and add them

# if = try
# elif = except specific error type
# else = except 

# Except only happens if something in try causes an error
try:
    x = int(input("What's first number?\n-"))
    y = int(input("What's second number?\n-"))
    print(x + y)
except:
    print("Invalid entry...")


def add_two_numbers():
    try:
        x = int(input("What's first number?\n-"))
        y = int(input("What's second number?\n-"))
        print(x + y)
    except:
        print("Invalid entry....")
        add_two_numbers

add_two_numbers()

def divide_two_numbers():
    try:
        x = int(input("What's first number?\n-"))
        y= int(input("What's second number?\n-"))
        print(x/y)
    except ValueError:
        print("Please enter a number....")
        divide_two_numbers()
    except ZeroDivisionError:
        print("Cannot divide by zero...")
        divide_two_numbers
    finally:
        print()
    
divide_two_numbers()
    
    
   
    




