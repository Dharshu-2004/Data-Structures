class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append_node(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end='->' if temp.next is not None else '\n')
            temp = temp.next

    def reverse_linked_list(self):
        cur=self.head
        prev=None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        self.head=prev
    

def create_linked_list():
    values = input("Enter the elements of the linked list separated by spaces: ").split()
    li = LinkedList()
    for i in values:
        li.append_node(int(i))
    return li

if __name__ == "__main__":
    li = create_linked_list()
    li.reverse_linked_list()
    li.print_list()
