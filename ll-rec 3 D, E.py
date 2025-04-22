def task_3E(head):
  temp = head
  sum = 0
  mul = 1
  while temp != None:
    if temp.elem % 2 != 0:
      sum += temp.elem
    else:
      mul *= temp.elem
    temp = temp.next
  return (sum - mul)

n1 = Node(1)
n2 = Node(3)
n3 = Node(4)
n4 = Node(9)
n5 = Node(1)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(task_3E(n1))
######################################

def task_3F(head):
  def helper(head,sum = 0, mul = 1):
    if head == None:
      return (sum - mul)
    if head.elem % 2 == 0:
      mul *= head.elem
    else:
      sum += head.elem
    head = head.next
    return helper(head,sum,mul)
  return helper(head)


n1 = Node(1)
n2 = Node(3)
n3 = Node(4)
n4 = Node(9)
n5 = Node(10)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(task_3F(n1))
