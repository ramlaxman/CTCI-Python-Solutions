from copy import deepcopy
from _utils import SingleLinkedList

# Runtime: O(n)
# Memory: O(1)
def partition(head, value):
    initial_tail = head.tail()
    current_tail = initial_tail
    current = head
    prev = None
    while current != initial_tail:
        node = current
        current = node.next
        if node.value >= value:
            if prev:
                prev.next = node.next
            else:
                # If there was no prev the head changed
                head = node.next
            current_tail.next = node
            node.next = None
            current_tail = node
        else:
            prev = node
    return head

if __name__ == '__main__':
    head = SingleLinkedList(3)
    node = head
    for x in [5, 8, 5, 10, 2, 1]:
        node.next = SingleLinkedList(x)
        node = node.next
    head2 = deepcopy(head)

    print('INITIAL\t\t', head)
    print('PARTITION\t', partition(head, 5))
    print('INITIAL\t\t', head2)
    print('PARTITION\t', partition(head2, 3))
