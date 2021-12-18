from linked_list import Node, LinkedList
import pytest

def test_node_instance():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1

def test_node_instance_fail():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2

def test_linked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node

def test_linked_list_empty():
    ll = LinkedList()
    assert ll.head == None

def test_insert_to_empty_linked_list():
    # ll.head = apple
    ll = LinkedList()
    ll.insert('apple')
    assert ll.head.value == 'apple'

def test_insert_to_linked_list():
    # ll
    # node1
    # node2
    # ll.head = apple
    # apple.next = pear
    # pear.next = None

    # [apple] -> [pear] -> None
    
    ll = LinkedList()
    # head is none
    node1 = Node('apple')
    # ll.head is none
    ll.head == node1
    # ll.head is apple
    node2 = Node('pear')
    # apple.next is none
    node1.next = node2
    # apple.next is pear
    # [apple] -> [pear] -> None
    ll.insert('bananna')
    # [bananna] -> [apple] -> [pear]
    assert ll.head.value == 'bananna'