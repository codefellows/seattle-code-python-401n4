def delete_over(ll, num):

    at_head_node = True
    current = ll.head

    while at_head_node and ll.head:
        if not ll.head.next and ll.head.value > num:
            ll.head = None
            return ll
        elif ll.head.value > num:
            ll.head = current.next
        else:
            at_head_node = False
    
    while current.next:
        previous = current
        current = current.next
        if current.value > num:
            previous.next = current.next
    return ll      