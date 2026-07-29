# This is not the Ideal solution to the problem but just a brute force solution to it which can be applied by those who only know operation on arrays in Python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode|None) -> ListNode|None:
        array = []
        current = head
    
    # Traverse the linked list until reaching the end (None)
        while current:
            array.append(current.val)  # Add current node's value to the array
            current = current.next
        for j in range(1, len(array)):
            key=array[j]#value of current element
            i=j-1#index of previous element
            while i>=0 and array[i]>key:
                array[i+1]=array[i]#giving the value of current element to the element at previous index
                i=i-1#pointing out the index to a prior element(i.e. j-2, j-3,....)
            array[i+1]=key
        dummy = ListNode(0) 
        current = dummy
    
        # Iterate and chain new nodes
        for item in array:
            current.next = ListNode(item)
            current = current.next
        
        # Return the actual head (skip dummy)
        return dummy.next