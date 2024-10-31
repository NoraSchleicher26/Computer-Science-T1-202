#Python has four types of collections
#Tuple
#Set
#List
#Dictionary

#Today we are are going to focus on lists
#A list is a way to store more than one value in a single variable
#Those values in the list are called ITEMS
#ITEMS can be accessed by their index (position in the list)
#INDEX                      0                    1            2                 3            4
best_elden_ring_weapons = ["Blaspehmous Blade", "Moonveil", "Rivers of Blood", "Iron Ball", "Bloodhound's Fang"]

#INDEX          0     1     2     3
best_years = [1776, 1985, 1994, 1957]

#Prints the index of the value in the list
print(best_years.index(1985))

#Print the best elden ring weapon
print(best_elden_ring_weapons[0])

#Print the worst of the best elden ring weapon
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])

#Tells us how many items are in list
#len is short for length
print(len(best_elden_ring_weapons))

#List items can be changed!
best_elden_ring_weapons[3] = "Spiked Fist"
print(best_elden_ring_weapons)

#Remove the last item in the list by its position in the list
#The .pop() function removes an item in a list by its position in the list
best_elden_ring_weapons.pop(4)
print(best_elden_ring_weapons)

#Remove an item by its value
best_elden_ring_weapons.remove("Moonveil")
print(best_elden_ring_weapons)

#Add a new item to the end of a list
#Append: make a new addition
best_elden_ring_weapons.append("Mohgwyn's Sacred Spear")
print(best_elden_ring_weapons)

import random
numbers = [random.randint(1,100),random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100) ]
print(numbers)
print(max(numbers))     #Prints highest number
print(min(numbers))     #Prints lowest number
numbers.sort()
print(numbers)

#Strings are lists!
#Strings are just a list of characters
word = "potato"
print(word[0])      #Prints "p"




