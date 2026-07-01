class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Singly_linkedList:
    def __init__(self):
        self.head = None
        
    def append(self, val):
        new_node = Node(val)
        # If linked list is empty
        if self.head==None:
            self.head=new_node
        
        # if linked list have some nodes
        else:
            curr_node = self.head
            while curr_node.next is not None: # here we are pointing next node's address
                curr_node = curr_node.next
            curr_node.next = new_node
    
    def traverse(self):
        if not self.head:
            print("Linked List is empty")
        else:
            curr_node=self.head
            while curr_node is not None: # here we are pointing node's value
                print(curr_node.val, end=" ")
                curr_node=curr_node.next
            print()

sll = Singly_linkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traverse()
