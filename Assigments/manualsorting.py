numbers1 = [87, 72, 6, 23, 45,52]

        

def bubble_sort(numbers1):
    steps = 0
    for j in range(0, len(numbers1)-1):
        for i in range(0, len(numbers1)-1):
            if numbers1[i] > numbers1[i+1]:
                a = numbers1[i]
                numbers1[i], numbers1[i+1] = numbers1[i+1], numbers1[i]
                steps += 1
            

    
    print(numbers1)
    print("Completed in " + str(steps) + " steps.")

bubble_sort(numbers1)




