class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value, end="->")
            temp=temp.next
            
    def middlenode(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
def create_linked_list():
    values=input("Enter the values seperated by comma").split()
    li=LinkedList()
    for i in values:
        li.append(int(i))
    return li
if __name__ == "__main__":
    li=create_linked_list()
   
    middlenodes=li.middlenode()
    print("The middle node is ",middlenodes.value)
    temp=middlenodes
    while temp is not None:
        print(temp.value,end="->")
        temp=temp.next
    print("None")