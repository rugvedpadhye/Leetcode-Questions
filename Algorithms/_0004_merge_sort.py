#merge sort is an sorting Algorithm, which works on the divide and conquer approach
# here we first divide the array into two halves and then sort them while merging

def merge(left,right):#main sorting and merging algorithm
    sorted_array=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            sorted_array.append(left[i])
            i+=1
        else:
            sorted_array.append(right[j])
            j+=1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

def merge_sort(array):#Algorithm for dividing the array into subparts
    mid=len(array)//2
    if len(array)<=1:
        return array
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])
    
    # Combine phase
    return merge(left_half, right_half)

arr=[11,31,41,59,26,41,58]
print(merge_sort(arr))