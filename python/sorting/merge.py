def printLinkedList(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(values)

def find_middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_lists(l1, l2):
    dummy = Node(0)
    head = dummy

    while l1 and l2:
        
        if l1.value < l2.value:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next

    head.next = l1 or l2
    return dummy.next


def mergesort(head):
    if not head or not head.next:
        return head
    
    middle = find_middle(head)
    after_middle = middle.next
    middle.next = None
    left = mergesort(head)
    right = mergesort(after_middle)

    sorted_list = merge_lists(left, right)

    return sorted_list
    
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node_7 = Node(7)
node_1 = Node(1, node_7)
node_3 = Node(3, node_1)
node_9 = Node(9, node_3)

printLinkedList(node_9)

my_list = mergesort(node_9)

printLinkedList(my_list)

