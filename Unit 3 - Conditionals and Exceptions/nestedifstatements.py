# Nested if statements
# If statement inside of another if statement
# You are a Prime member OR order is at least $25
# You are at least 18 years old OR have parent consent

prime = True
cost = 20
age = 17
consent = False

if prime:
    if age >= 18:
        print("You are eligible for free shipping!")
    elif consent:
        print("You are eligible for free shipping!")
    else:
        print("You are NOT eligible for free shipping!")
elif cost >= 25:
    if age >= 18 :
        print("You are elgiible for free shipping!")
    elif consent:
        print("You are eligible for free shipping!")
    else: 
        print("You are NOT eligible for free shipping!")
else:
    print("You are NOT eligible for free shipping!")


# Do we need an umbrella?

# We need an umbrella if it is raining and we are outside
    
raining = input("Is it raining today?\n-")


# Using nested if statements
if raining.lower() == "yes":
    outside = input("Are you going outside today?\n-")

    if outside.lower() == "yes":
        print("Bring an umbrella")
    else:
        print("Don't bring an umbrella")
else:
    print("Don't bring an umbrella")

# Using logical operators
if raining and outside:
    print("Bring an umbrella")

else:
    print("Don't bring an umbrella")

    