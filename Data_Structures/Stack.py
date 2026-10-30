class Node:
    def __init__(self: Node, data: int)->None:
        self.data: int=data
        self.next: Node|None=None
class Stack:
    def __init__(self: Stack)->None:
        self.top=None

    def push(self: Stack,data: int)->None:
        newNode: Node=Node(data)
        if self.is_empty():
            self.top=newNode
            return
        assert self.top is not None
        self.top=self.top.next
    

    def display(self: Stack)-> None:
        if self.is_empty():
            print("Stack is Empty")
            return
        temp: Node|None= self.top
        assert self.top is not None
        while self.top.next is not None:
            print(self.top.data, end=" -> ")
            self.top=self.top.next
        print("End")

    def is_empty(self: Stack)-> bool:
        if self.top is None:
            return True
        return False

stack: Stack= Stack()
stack.display()
stack.push(1)
stack.push(11)
stack.display()
stack.push(22)
stack.push(33)
stack.display()