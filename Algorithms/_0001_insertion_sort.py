# Insertion sort is a sorting method where we loop out through the array pick one element at a time(named as key) and then compare it with elements prior to it in the array

arr=[11,31,41,59,26,41,58]

def insertion_sort_inc(array):
    for j in range(1, len(array)):
        key=array[j]#value of current element
        i=j-1#index of previous element
        while i>=0 and array[i]>key:
            array[i+1]=array[i]#giving the value of current element to the element at previous index
            i=i-1#pointing out the index to a prior element(i.e. j-2, j-3,....)
        array[i+1]=key
    return array

def insertion_sort_dec(array):
    for j in range(1, len(array)):
        key=array[j]#value of current element
        i=j-1#index of previous element
        while i>=0 and array[i]<key:
            array[i+1]=array[i]#giving the value of current element to the element at previous index
            i=i-1#pointing out the index to a prior element(i.e. j-2, j-3,....)
        array[i+1]=key
    return array

print(insertion_sort_inc(arr))
print(insertion_sort_dec(arr))