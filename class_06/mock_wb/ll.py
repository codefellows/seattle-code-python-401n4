# Mock Question

# Given a linked_list, iterate the linked list and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3) expected return (13)

def largest_value(ll):
  largest = 0
  current = ll.head
  while current:
    if current.value > largest:
      largest = current.value
    current = current.next

  return largest
