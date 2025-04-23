#task 4
def task4A_recursive(head):
  # def leng(head,c = 0):
  #   if head == None:
  #     return c
  #   else:
  #     c+=1
  #   head = head.next
  #   return leng(head, c)
  # def helper (head , i = leng(head)):
  #   if head == None:
  #     return
  #   else:
  #     print(head[i],end = " --→")
  #   helper(head)
  # return helper
  
  if head == None:
    return
  task4A_recursive(head.next)
  print(head.elem,end="--→")


n1 = Node(1)
n2 = Node(3)
n3 = Node(4)
n4 = Node(9)
n5 = Node(10)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

task4A_recursive(n1)


###################################################
#task4B_recursive

def task4B_recursive(head):
  if head == None or head.next == None:
    return head
  new_head = task4B_recursive(head.next)

  # head.next.next = head
  temp = head.next
  temp.next = head
  head.next = None
  
  return new_head

def print_list(head):
    while head is not None:
        print(head.elem, end=" → ")
        head = head.next
    print("None")

n1 = Node(1)
n2 = Node(3)
n3 = Node(4)
n4 = Node(9)
n5 = Node(10)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print_list(task4B_recursive(n1))
