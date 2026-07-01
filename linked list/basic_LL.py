class Node:
    def __init__(self, val):
        self.val=val
        self.next = None
        
# Node Creation
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Linking Node with each other
node1.next = node2
node2.next = node3
node3.next = node4

# # if we print an object it shows memory address
# print(node1.val)
# print(node1.next.next.next.val)
# print(node1.next) # memory address of node2
# print(node2) 
# print(node2.val)
