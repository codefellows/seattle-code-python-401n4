# Given a BST and a value, determine if any root to leaf sum is the same as the given value.  Return true of false


def leaf_to_root(root, val):

    def walk(root, total):
        if root is None:
            return total

        total = total + root.value

        if root.left is None and root.right is None:
            return total

        return (walk(root.left, total) +
                walk(root.right, total))

    return walk(root, 0) == val or False
