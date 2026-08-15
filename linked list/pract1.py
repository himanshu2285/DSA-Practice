# creating a linked list node

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class SingleLL:
    # creatinng Head of LL - By default head is empty
    def __init__(self):
        self.head=None
    
    # method to append nodes
    def append(self, val):
        new_node = Node(val)
        # To append value in linked list we have to condition
        # 1. head is empty
        # 2. head have some nodes
        
        if self.head==None:
            self.head=new_node
        else:
            curr_node=self.head
            while curr_node.next is not None:
                curr_node=curr_node.next
            curr_node.next=new_node
    
    # method to display the nodes
    def traverse(self):
        if not self.head:
            print('linked list is empty')
        else:
            curr_node=self.head
            while curr_node is not None:
                print(curr_node.val, end=' ')
                curr_node=curr_node.next
            print()
            
    
    # method to insert at specific position
    def insert_at(self, val, position):
        new_node = Node(val)
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
        if curr_node.next is not None:
            if curr_node.val==val:
                self.head=curr_node.next
                return
            else:
                found=False
                prev_node=None
                while curr_node.val is not None:
                    if curr_node.val==val:
                        found=True
                        break
                    prev_node=curr_node
                    curr_node=curr_node.next
                
                if found:
                    prev_node.next=curr_node.next
                    return
                else:
                    print('node not found')
                

obj = SingleLL()
# obj.traverse()
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.insert_at(10,3)
obj.insert_at(12,3)
obj.delete(1)
obj.traverse()
