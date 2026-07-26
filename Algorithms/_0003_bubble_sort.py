# This is an sorting algorithm where your compare two adjacent elements and sort them and move forward

arr=[12, 8, 11, 14, 21, 94, 74, 65, 32, 32]

def bubble_sort(array):
    n = len(array)
    # Outer loop for each pass through the list
    for i in range(n):
        # Track if any swaps happen in this pass
        swapped=False      
        # Inner loop to compare adjacent elements
        # Last i elements are already in place, so we skip them
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                # Swap elements using Pythonic tuple unpacking
                array[j],array[j+1]=array[j+1],array[j]
                swapped=True
                
        # If no elements were swapped, the list is already sorted
        if not swapped:
            break
    return array
print(bubble_sort(arr))