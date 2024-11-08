#Dictionary is a type of collection like list
#A list is a collection of items in a sequence
#A Dictionary is different
#Dictionaries store data in key-value pairs
#You can retrieve data quickly by using a unique key
#Instead of retrieving it by index (position)

#Example
#Lists use brackets, dictionaries use braces
nora = {
    "name": "Nora",
    "age": 16,
    "city": "St. Michael",
    "pets": 1,
    "height": 5.6
}
#Each key must be unique

#Retreiving values from a dictionary
#.get allows you to retrieve a value without erroring
#when the key doesn't exist
#second parameter is what is given if value is not found
print(nora["age"])
print(nora.get("height"))

#You can add values to a dictionary

nora["country"] = "USA"

#You can modify values
nora["age"] = 17

print(nora)

#Remove entries
nora.pop("pets")


#Iterate through a dictionary usinga for loop

for key, value in nora.items():
    print(key + ": " + str(value))

#Dictionary functions
print(nora.keys())      #returns all keys
print(nora.values())        #returns all values
print(nora.items())     #returns all pairs
print(nora.clear())     #removes all items from the dictionary

