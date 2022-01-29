class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # ll head of 1
    # [1] -> [2] -> None
    # insert 3
    # ll know the head 3
    # [3] -> [1] -> [2] -> None
    
    def insert(self, value):
        node = Node(value) # Node of [3]
        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self):
        pass

    def to_string(self):
        pass
