class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
#To create a Node
    
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail = new_node
        self.length = 2
#This will create a node in a linked List where the single node is created here, so that will be a
#head node and tail node.
obj=LinkedList(4)
print("The value of the first node in the Linked List is ",obj.head.value)