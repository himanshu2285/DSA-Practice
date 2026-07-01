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
            
    def insert_at(self, val, position):
        new_node=Node(val)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            curr_node=self.head
            prev_node=None
            count=0
            while curr_node is not None and count<position:
                prev_node=curr_node
                curr_node=curr_node.next
                count+=1
            prev_node.next=new_node
            new_node.next=curr_node
            
    def delete(self, val):
        curr_node=self.head
        # if we have to delete first value
        if curr_node.next is not None:
            if curr_node.val==val:
                self.head=curr_node.next
                return
            else:
                found=False
                prev_node=None
                while curr_node is not None:
                    if curr_node.val==val:
                        found=True
                        break
                    prev_node=curr_node
                    curr_node=curr_node.next
                
                if found:
                    prev_node.next=curr_node.next
                    return 
                else:
                    print('Node not found')

sll = Singly_linkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(35)
# sll.insert_at(35, 3)
# sll.insert_at(5, 0)
sll.insert_at(40, 4)
sll.traverse()

sll.delete(35)
sll.traverse()
