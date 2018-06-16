class LinkedList:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        values = []
        node = self
        while node:
            values.append(str(node.value))
            node = node.next
        return '->'.join(values)

    def remove(self):
        if self.prev:
            self.prev.next = self.next
            if self.next:
                self.next.prev = self.prev
                


def print_matrix(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
