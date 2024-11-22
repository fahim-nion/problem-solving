'''
Given a singly linked list and a number num, rotate the linked list from
the end so that the last num elements are reversed and appended at the
end of the list. Assume num is always less than the length of the 
linked list.

Example:
Input:
Linked List: 1 -> 2 -> 3 -> 4 -> 5
num = 4

Output:
1 -> 5 -> 4 -> 3 -> 2
'''
class Node:
    def __init__ (self,elem,next=None):
        self.elem = elem
        self.next = next

def length(head):
    length = 0 
    temp = head

    while temp != None:
        length +=1
        temp = temp.next
    return length

def rotate_backward(head,num):
    split_point = length(head)-num
    if split_point == 0:
        return head
    
    current = head
    for _ in range(split_point-1):
        current = current.next

    prev = None
    curr = current.next
    nxt = None

    while curr!= None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    current.next = prev
    return head



def print_linked_list(head):
    temp = head
    while temp:
        print(temp.elem, end=" -> " if temp.next else "\n")
        temp = temp.next



# Create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Input number
num = 2

# Rotate the linked list
print("Original List:")
print_linked_list(head)

result = rotate_backward(head, num)
print("Rotated List:")
print_linked_list(result)