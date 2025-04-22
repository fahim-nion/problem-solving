#task 3C

def task_3C(head):
  def helper(head,sum = 0):
    if head == None:
      return sum
    sum += head.elem
    head = head.next
    return helper(head,sum)
  return helper(head)
  

n1 = Node(10)
n2 = Node(20)
n3 = Node(40)

n1.next = n2
n2.next = n3


print(task_3C(n1))
