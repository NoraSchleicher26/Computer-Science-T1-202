#Bubble Sort:
print("Bubble Sort:")
numbers1 = [87, 72, 6, 23, 45,52]       #Number list

print(numbers1)     #Print the list before it is sorted     

def bubble_sort(numbers1):      #Define function and take the list as a parameter
    steps = 0       #Create variable for how many steps we are taking, start at 0
    for j in range(0, len(numbers1)-1):     #Check if the list is sorted as many times as their are list items
        #iterate through every item in list
        for i in range(0, len(numbers1)-1):
            #Check if the current list item is greater than the next list item
            if numbers1[i] > numbers1[i+1]:
                #Swap values if needed
                a = numbers1[i]
                numbers1[i], numbers1[i+1] = numbers1[i+1], numbers1[i]
                steps += 1      #Increase number of steps
            

    
    print(numbers1)#        Print sorted list
    print("Completed in " + str(steps) + " steps.")     #Print number of steps

bubble_sort(numbers1)       #Run function

print("----------------------------------")
#Quick Sort:
print("Quick Sort:")
numbers2 = [65, 8, 90, 23]      #Number list

print(numbers2)     #Print the list before it is sorted

def quick_sort(numbers2):       #Define function and take the list as a parameter
    steps = 0       #Create variable for how many steps we are taking, start at 0
    lPos = 0
    rPos = len (numbers2)-1
    #set pivot as the last number
    pivot = numbers2[-1]
    for j in range(0, len(numbers2)):
        #Find l
        #first number from the left that is LARGER
        #first number from the right that is SMALLER
        for i in range(0, len(numbers2)):
            if i> pivot:
                lPos = i
                break

        #find r
        for i in range(len(numbers2)-1, -1, -1):
            if numbers2[i] < pivot:
                rPos = i
                break
        #check if L index is greater than r index
            if lPos>rPos:
                numbers2[lPos], numbers2[-1] = numbers2[-1], numbers2[lPos]
                break
            else:
                numbers2[lPos], numbers2[rPos] = numbers2[rPos], numbers2[lPos]
        #swap l and r values
        numbers2[lPos], numbers2[rPos] = numbers2[rPos], numbers2[lPos]
    
    
    print(numbers2)

quick_sort(numbers2)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


    

    




