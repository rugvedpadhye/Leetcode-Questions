class Node:
    def __init__(self: Node, data: int) -> None:
        self.prev: Node|None=None
        self.data: int=data
        self.next: Node|None=None


class DoublyLinkedList:
    def __init__(self: DoublyLinkedList) -> None:
        self.head: Node|None=None


    def is_empty(self: DoublyLinkedList)->bool:
        if self.head is None:
            return True
        return False