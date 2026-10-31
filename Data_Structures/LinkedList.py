class Node:
    def __init__(self: Node, data: int)->None:
        self.data: int=data
        self.next: Node|None=None

class LinkedList:
    def __init__(self: LinkedList)->None:
        self.head: Node|None=None


    def insert_end(self: LinkedList, data: int)->None:
        newNode: Node=Node(data)
        if self.is_empty():
            self.head=newNode
            return
        temp: Node|None=self.head
        assert temp is not None
        while temp.next is not None:
            temp=temp.next
        temp.next=newNode


    def insert_begin(self: LinkedList, data: int)->None:
        newNode: Node=Node(data)
        if self.is_empty():
            self.head=newNode
        newNode.next=self.head
        self.head=newNode

    
    def delete_end(self: LinkedList)->None:
        if self.is_empty():
            print("List is Empty")
            return
        temp: Node|None=self.head
        assert temp is not None
        temp1: Node|None=temp.next
        assert temp is not None
        while temp1 is not None:
            temp1=temp1.next
        temp.next=None


    def delete_begin(self: LinkedList)->None:
        if self.is_empty():
            print("List is Empty")
            return
        assert self.head is not None
        self.head=self.head.next     
            

    def display(self: LinkedList)->None:
        temp: Node|None=self.head
        if self.is_empty():
            print("List is Empty")
            return
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next  # Safe because the while condition ensures temp is a Node
        print("End")


    def is_empty(self: LinkedList)->bool:
        if self.head is None:
            return True
        return False


# Running Tests
# LL1: LinkedList=LinkedList()
# LL1.display()
# LL1.insert_end(10)
# LL1.insert_end(20)
# LL1.insert_begin(00)
# LL1.insert_end(30)
# LL1.display()
# LL1.delete_begin()
# LL1.delete_begin()
# LL1.display()
# LL1.delete_end()
# LL1.display()