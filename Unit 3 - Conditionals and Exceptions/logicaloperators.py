# Logical Operators: and or ! 
# Comparison operator s> < == >= <=
# Arithmetic operators + - / * % ** //

def check_eligibility (age, exp):
    # You must be at least 18 years old and have 1 year of experience to be eligible
    if age >= 18 and exp >= 1:  #Must have complete boolean expressions on both sides
        print("You are eligible for the competition!")
    elif age < 18:
        print("You are not old enough to compete.")
    elif exp < 1:
        print("You don't have enough experience to compete")

a = int(input("How old are you\n-"))
e= int(input("How many years of experience do you have?\n-"))

check_eligibility (a, e)

