numbers1 = [87, 72, 6, 23, 45,52]       #Number list

print(numbers1)     #Print the list before it it started     

def bubble_sort(numbers1):      #Define function and take the list as a parameter
    steps = 0       #Create variable for how many steps we are taking, start at 0
    for j in range(0, len(numbers1)-1):     #Check if the list is sorted as many times as their are list items
        #iterate through every item in list
        for i in range(0, len(numbers1)-1):
            #check if the current list item is greater than the next list item
            if numbers1[i] > numbers1[i+1]:
                #swap values if needed
                a = numbers1[i]
                numbers1[i], numbers1[i+1] = numbers1[i+1], numbers1[i]
                steps += 1#increase number of steps
            

    
    print(numbers1)#print sorted list
    print("Completed in " + str(steps) + " steps.")#print number of steps

bubble_sort(numbers1)#Run function




