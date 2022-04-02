def bst_contains(input_tree, value):
  node = input_tree.root
  while node is not None:
    if value == node.value:
      return True
    elif value < node.value:
      node = node.left
    else:
      node = node.right
  return False