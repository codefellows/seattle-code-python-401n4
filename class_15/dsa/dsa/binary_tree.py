class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        # root > left > right
        #           A
        #       /       \
        #      B         C
        #   /    \     /   
        #  D     E    F   

        # Expect A B D E C F

        # empty list for values
        values = []

        def walk(root):
            if root is None:
                return

            values.append(root.value)
            walk(root.left)
            walk(root.right)

        walk(self.root)
        return values



    def in_order():
        # left > root > right
        pass

    def post_order():
        # left > right > root
        pass