from dsa import __version__
from dsa.node import Node
from dsa.binary_tree import BinaryTree


def test_version():
    assert __version__ == '0.1.0'

def test_new_node():
    node = Node(11)
    actual = node.value
    expected = 11
    assert actual == expected

def test_new_node_bad():
    node = Node(11)
    actual = node.value
    expected = 12
    assert actual != expected

def test_bt_empty():
    bt = BinaryTree()
    assert bt

def test_bt_empty_root_none():
    bt = BinaryTree()
    assert bt.root == None


def test_bt_left_right():
    
#           apple
#       /           \
#   pear          orange  


    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')

    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange

    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.pre_order()
    assert order_list == ['apple', 'pear', 'orange']


