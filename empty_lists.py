LINKED LIST APPEND AND PRINT

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
        self.length = 1
    
    def printList(self):
        temp=self.head
        while temp is not None:
           print(temp.value)
           temp=temp.next
    def make_empty(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def appendnode(self,value):
        new_node=Node(value)
        if self.length == 0:
          '''If the Linked List is empty'''
          self.head = new_node
          self.tail=new_node
        else:
            '''If the Linked List is not empty'''
            self.tail.next=new_node
            self.tail = new_node
        self.length += 1
        


obj=LinkedList(4)
print("The value of the head node in the Linked List is ",obj.head.value)
obj.appendnode(11)
obj.appendnode(31)
obj.appendnode(15)
obj.printList()
print("after empty the linked List is ")
obj.make_empty()
obj.printList()

output:
The value of the head node in the Linked List is  4
4
11
31
15
after empty the linked List is 