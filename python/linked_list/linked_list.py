class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node

        self.head = new_node
        


    def add_to_end(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node

    def remove_to_front(self):
        if self.head is None:
            return None
        
        removed_value = self.head.value
        
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        
        return removed_value

    def remove_to_end(self):
        if self.tail is None:
            return None
        
        removed_value = self.tail.value
        
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        
        return removed_value
    

dll = DoubleLinkedList()

dll.add_to_front(3)
dll.add_to_front(2)
dll.add_to_front(1)
dll.add_to_end(4)
dll.add_to_end(5)

print(dll.remove_to_front())
print(dll.remove_to_end())
print(dll.remove_to_front())
print(dll.remove_to_end())