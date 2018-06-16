from _utils import SingleLinkedList

def kth_from_last(head, k):
    node = head
    runner = node
    for i in range(k):
        if runner.next:
            runner = runner.next
        else:
            return None
    while runner.next:
        node = node.next
        runner = runner.next
    return node

if __name__ == '__main__':
    head = SingleLinkedList(0)
    node = head
    for value in [1, 2, 3, 4, 5]:
        node.next = SingleLinkedList(value)
        node = node.next
    print(kth_from_last(head, 0))
    print(kth_from_last(head, 2))
    print(kth_from_last(head, 5))
    print(kth_from_last(head, 7))
