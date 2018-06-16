class SingleLinkedList:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        values = []
        node = self
        while node:
            values.append(str(node.value))
            node = node.next
        return '->'.join(values)

    def tail(self):
        node = self
        while node.next:
            node = node.next
        return node

    def remove(self, prev):
        prev.next = self.next


class DoubleLinkedList(SingleLinkedList):
    def __init__(self, value=None, prev=None, next=None):
        self.prev = prev
        SingleLinkedList.__init__(self, value=value, next=next)

    def remove(self):
        if self.prev:
            self.prev.next = self.next
            if self.next:
                self.next.prev = self.prev



def print_matrix(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
