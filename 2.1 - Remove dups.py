from copy import deepcopy
from _utils import DoubleLinkedList

# Runtime: O(n)
# Memory: O(n)
def remove_dups_hash(head):
    seen = set()
    node = head
    while node:
        if node.value in seen:
            node.remove()
        else:
            seen.add(node.value)
        node = node.next
    return head

# Runtime: O(n^2)
# Memory: O(1)
def remove_dups_runner(head):
    node = head
    while node:
        runner = node.next
        while runner:
            if node.value == runner.value:
                runner.remove()
            runner = runner.next
        node = node.next
    return head

if __name__ == '__main__':
    head = DoubleLinkedList(0)
    node = head
    for value in [1, 3, 3, 3, 0, 5, 1, 2, 3, 4, 0, 2, 2, 2, 2, 2]:
        node.next = DoubleLinkedList(value, node)
        node = node.next
    print(remove_dups_hash(deepcopy(head)))
    print(remove_dups_runner(deepcopy(head)))
