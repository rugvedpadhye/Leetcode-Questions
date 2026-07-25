#This algorithm is an sorting algorithm, where you first find the smallest element in the array and replace it at first index(i.e. arr[0]) and then find the next smallest element and replace it with second index(arr[1])

arr=[12, 8, 11, 14, 21, 94, 74, 65, 32, 32]

def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(0,n-1):
        # Assume the current position is the minimum
        min_idx=i
        # Test against the remaining unsorted elements
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j        
        # Swap the found minimum element with the first unsorted element
        if min_idx!=i:
            arr[i],arr[min_idx]=arr[min_idx],arr[i]        
    return arr

print(selection_sort(arr))