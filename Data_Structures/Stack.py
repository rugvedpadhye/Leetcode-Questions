class Node:
    def __init__(self: Node, data: int)->None:
        self.data: int=data
        self.next: Node|None=None
        
class Stack:
    def __init__(self: Stack)->None:
        self.top: Node|None=None


    def is_empty(self: Stack)-> bool:
            if self.top is None:
                return True
            return False


    def push(self: Stack, data: int) -> None:
        newNode: Node = Node(data)
        newNode.next = self.top
        self.top = newNode


    def pop(self: Stack)->None:
        if self.is_empty():
            print("Stack is Empty")
            return
        assert self.top is not None
        self.top=self.top.next


    def peek(self: Stack)->None:
        if self.is_empty():
            print("Stack is Empty")
            return
        assert self.top is not None
        print(f"Top: {self.top.data}")
    

    def display(self: Stack) -> None:
        if self.is_empty():
            print("Stack is Empty")
            return
        temp: Node | None = self.top
        print("Top-> ", end="")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("End")
    

stack: Stack= Stack()
stack.display()
stack.pop()
stack.push(1)
stack.push(11)
stack.peek()
stack.display()
stack.push(22)
stack.push(33)
stack.display()
stack.peek()
stack.pop()
stack.display()