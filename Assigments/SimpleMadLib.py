#Today I went to {Place}
#and saw a {Adjective} racoon
#{Verb} through trash.
#Then I saw {Person} 
#carry {Number} {Plural Noun}
#all the way over to the trash can and laugh at the raccoon.
#The {Number" {Plural Noun} fell in the trash.
#The {Adjective2} and {Adjective3}
#racoons were then {Verb2} through the mess
Place = input("Write a place\n-")       #Ask user for place to fill mad lib
Adjective = input("Write an adjective\n-")      #Ask user for Adjective to fill mad lib
Verb = input("Write a verb ending in ing\n-")       #Ask user for Verb to fill mad lib
Person = input("Write a person's name\n-")      #Ask user for name of person to fill mad lib
Number = input("Write a number\n-")     # Ask user for random number to fill mad lib
PluralNoun = input("Write a plural noun\n-")        #Ask user for plural noun to fill mad lib
Adjective2 = input("Write another adjective\n-")        #Ask user for another adjective to fill mad lib
Adjective3 = input("Write another adjective\n-")        #Ask user for another adjective to fill mad lib
Verb2 = input("Write another verb ending in ing\n-")        #Ask user for another verb ending in ing to fill mad lib
print (" Today I went to " + Place + " and saw  " + Adjective + " racoons " + Verb + " through trash. " + " Then I saw " + Person + " carry " + Number + " " + PluralNoun + " all the way over to the trash can and laugh at the racoon. " + " The " + Number + " " + PluralNoun + " fell in the trash. " + " The " + Adjective2 + " and " + Adjective3 + " raccons were then " + Verb2 + " through the mess. ")        #print summary of users in answers in fun fill in the blank random mad lib