#        {a}
#       /  \
#    {b}    {c}
#    /      / \
#  {d}    {e} {f}

# BFS -> a-b-c-d-e-f
# Expected -> f-e-d-c-b-a
# node -> stack
#----------------------
#                      
#----------------------
# Stack: 
def print_reversed(tree):
    # go through the bfs put to a stack then pop off the stack and print
    queue = Queue()
    stack = Stack()

    # This puts the root into the queue
    queue.enqueue(tree.root) 

    while queue.is_empty() is False:
        node = queue.dequeue() # grabbing the value adding to another node
        stack.push(node.value)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    while stack.is_empty() is False:
        print(stack.pop())

# Print: f e d c b a