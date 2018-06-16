from _utils import LinkedList

def remove_dups_hash(head):
    seen = set()
    node = head
    while node:
        if node.value in seen:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        else:
            seen.add(node.value)
        node = node.next
    return head

if __name__ == '__main__':
    head = LinkedList(0)
    node = head
    for value in [1, 3, 3, 3, 0, 5, 1, 2, 3, 4, 0, 2, 2, 2, 2, 2]:
        node.next = LinkedList(value, node)
        node = node.next
    print(remove_dups_hash(head))
