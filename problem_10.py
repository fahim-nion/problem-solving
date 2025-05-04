import numpy as np

class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


def sum_pair_finder(head, sum_val):
    def length_of_linked_list(head):
        temp = head
        c = 0
        while temp:
            c += 1
            temp = temp.next
        return c

    max_pairs = length_of_linked_list(head) * (length_of_linked_list(head) - 1) // 2
    pairs_array = np.zeros((2 * max_pairs), dtype=int)

    p = head
    counter = 0

    while p:
        q = p.next
        while q:
            if p.elem + q.elem == sum_val:
                pairs_array[counter], pairs_array[counter + 1] = p.elem, q.elem
                counter += 2
            q = q.next
        p = p.next

    return pairs_array[:counter]


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

print("Original List:")
print_linked_list(head)

# Find pairs that sum up to 5
result = sum_pair_finder(head, 5)

print("\nPairs that sum to 5:")
# Display the pairs stored in the NumPy array
for i in range(0, len(result), 2):
    print(f"({result[i]}, {result[i + 1]})")











rough


import numpy as np
class Node:
    def __init__(self,elem,next=None):
        self.elem = elem
        self.next = next


def sum_pair_finder(head,sum_val):
    def len(head):
        temp = head
        c = 0
        while temp!= None:
            c+=1
            temp = temp.next
        return c
    new = np.array([0]*(2*len(head)),dtype=int)
    p = head
    # q = None
    counter = 0
    while p!= None:
        q = p.next
        while q!= None:
            if p.elem + q.elem == sum_val:
                new[counter] ,new[counter+1] = p.elem,q.elem
                counter+=2
            q = q.next
        p = p.next
    non_zero = 0
    for i in new:
        if i!=0:
            non_zero+=1
        else:
            return []
    return new[:non_zero]












def print_linked_list(head):
    temp = head
    while temp:
        print(temp.elem, end=" -> " if temp.next else "\n")
        temp = temp.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


print("Original List:")
print_linked_list(head)

result = sum_pair_finder(head, 5)
print("Rotated List:")
print_linked_list(result)

# Display the pairs stored in the NumPy array
for i in range(0, len(result), 2):
    print(f"({result[i]}, {result[i+1]})")


