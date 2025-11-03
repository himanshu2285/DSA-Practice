# creating a linked list node

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

head = Node(1)
print(head.value)  
print(head.next)