import numpy as np

class CircularQueue:
    def __init__(self: CircularQueue, size: int):
        list=np.zeros(size)
        self.front=-1
        self.rear=-1

    