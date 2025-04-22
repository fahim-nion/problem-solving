class Node:
  def __init__(self, elem, next=None):
    self.elem = elem
    self.next = None


def task_3A(head):
  temp = head

  while temp != None:
    print(temp.elem,end = "--→")
    temp = temp.next

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3


task_3A(n1)
