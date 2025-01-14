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

    def swap_nodes(self):
        if self.head is None or self.head.next is None:
            return self.head

        p1 = self.head
        p2 = p1.next
        self.head = p2

        while True:
            p3 = p2.next
            p2.next = p1
            if p3 is None or p3.next is None:
                p1.next = p3
                break
            p1.next = p3.next
            p1 = p3
            p2 = p1.next

        return self.head

def create_linked_list():
    values = input("Enter the elements of the linked list separated by spaces: ").split()
    li = LinkedList()
    for i in values:
        li.append_node(int(i))
    return li

if __name__ == "__main__":
    li = create_linked_list()
    li.swap_nodes()
    li.print_list()
