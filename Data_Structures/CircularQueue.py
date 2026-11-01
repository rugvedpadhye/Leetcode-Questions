class Node:
    def __init__(self: Node, data: int)->None:
        self.data: int=data
        self.next: Node|None=None

class CircularQueue:
    def __init__(self: CircularQueue)->None:
        self.front: Node|None=None
        self.rear: Node|None=None


    def is_empty(self: CircularQueue)->bool:
        if self.front is None and self.rear is None:
            return True
        assert self.front is not None
        if self.front.next is self.rear:
            return False
        return False


    def enqueue(self: CircularQueue, data: int)->None:
        newNode: Node=Node(data)
        if self.is_empty():
            self.front=self.rear=newNode
            return
        assert self.rear is not None
        self.rear.next=newNode
        self.rear=newNode


    def dequeue(self: CircularQueue)->None|int:
        if self.is_empty():
            print("CircularQueue is Empty")
            return
        assert self.front is not None
        self.front=self.front.next


    def display(self: CircularQueue)->None:
        if self.is_empty():
            print("CircularQueue is Empty")
            return
        temp: Node|None=self.front
        assert temp is not None
        print("start->", end=" ")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp=temp.next
        print("rear")


# # Running Tests:
# q1: CircularQueue=CircularQueue()
# q1.display()
# q1.enqueue(0)
# q1.enqueue(10)
# q1.enqueue(20)
# q1.enqueue(30)
# q1.display()
# q1.dequeue()
# q1.display()