def loop_size(node):
    if not node or not node.next:
        return 0
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    contador = 1
    temp = slow.next
    while temp != slow:
        contador += 1
        temp = temp.next
    return contador