from _utils import SingleLinkedList

# Runtime: O(1)
# Memory: O(1)
def remove_middle(node):
    # Is not tail
    if node.next:
        node.value = node.next.value
        if node.next.next:
            node.next = node.next.next
        else:
            node.next = None

if __name__ == '__main__':
    head = SingleLinkedList(0)
    node = head
    for i in range(1, 5):
        node.next = SingleLinkedList(i)
        node = node.next
    node = head
    for i in range(3):
        node = node.next
    print(head)
    remove_middle(node)
    print(head)
    # Does not delete tail
    remove_middle(node)
    print(head)
    remove_middle(head.next)
    print(head)
