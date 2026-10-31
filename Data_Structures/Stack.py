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
stack.push(1)
stack.push(11)
stack.display()
stack.push(22)
stack.push(33)
stack.display()