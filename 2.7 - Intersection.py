from _utils import SingleLinkedList

# Runtime: O(N * M)
# Memory: O(1)
def intersect_naive(node1, head2):
    node2 = head2
    while node1:
        node2 = head2
        while node2:
            if node1 is node2:
                return node1
            node2 = node2.next
        node1 = node1.next

    return None

if __name__ == '__main__':
    head1 = SingleLinkedList.build([1, 2, 3, 4])
    head2 = SingleLinkedList.build([2, 3, 4])

    print(intersect_naive(head1, head2))

    tail = SingleLinkedList.build([5, 6, 7])
    head1.tail().next = tail
    head2.tail().next= tail
    print(intersect_naive(head1, head2))
