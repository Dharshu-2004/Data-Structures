class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def appendnode(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length +=1
        return True
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def popnode(self):
        if self.length==0:
            print("the linkedlist is empty")
        else:
            pre=self.head
            temp=self.head
            while(temp.next):
               pre=temp
               temp=temp.next
            self.tail=pre
            self.tail.next=None
            self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        self.printlist()
        
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        
    def popfirst(self):
         if self.length==0:
             print("the linked list is empty")
        
         temp=self.head
         self.head=temp.next
         temp=None
         self.length-=1
         if self.length==0:
             self.head=None
             self.tail=None
         self.printlist()
         
    def get(self,index):
        if(index < 0 or index >= self.length):
            return None
        temp = self.head
        for _ in range(index):
            temp=temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self,index,value):
        if (index < 0 or index > self.length):
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.appendnode(value)
        new_node=Node(value)
        temp=self.get(index - 1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True
        
    def remove(self,index):
        if (index <0 or index > self.length):
            return None
        if index==0:
            return self.popfirst()
        if index==self.length-1:
            return self.pop()
        pre=self.get(index-1)
        temp=prev.next
        prev.next=temp.next
        temp.next=None
        self.length-=1
        return temp
    
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
obj=LinkedList(4)
obj.appendnode(19)
obj.appendnode(15)
obj.appendnode(31)
print("before reversing a value")
obj.printlist()
print("after reversing a value")
obj.reverse()
obj.printlist()
