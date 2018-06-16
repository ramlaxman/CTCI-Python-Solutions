from _utils import SingleLinkedList

# Runtime O(n + m)
# Memory O(1)
def sum(n1, n2):
    current1, current2 = n1, n2
    remainder = 0
    prev = current1
    while current1 and current2:
        total = current1.value + current2.value + remainder
        current1.value = total % 10
        remainder = total // 10
        prev = current1
        current1 = current1.next
        current2 = current2.next

    not_finished = current1 or current2
    if not_finished:
        prev.next = not_finished
        current1 = not_finished
        while remainder and current1:
            total = current1.value + remainder
            current1.value = total % 10
            remainder = total // 10
            prev = current1
            current1 = current1.next

    if not current1 and remainder:
        prev.next = SingleLinkedList(remainder)
    return n1

if __name__ == '__main__':
    head1 = SingleLinkedList(1)
    node = head1
    for x in [1, 1, 4, 0, 3, 9, 9, 9]:
        node.next = SingleLinkedList(x)
        node = node.next

    head2 = SingleLinkedList(1)
    node = head2
    for x in [1, 1, 9, 9, 0, 4, 9, 9]:
        node.next = SingleLinkedList(x)
        node = node.next

    print('\t' + str(head1))
    print('+\t' + str(head2))
    print('\t' + str(sum(head1, head2)))
