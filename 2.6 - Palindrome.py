from _utils import SingleLinkedList

# Runtime: O(n)
# Memory: O(n)
def palindrome(head):
    stack = []
    length = 0
    cur = head
    while cur:
        stack.append(cur.value)
        length += 1
        cur = cur.next

    for i in range(length // 2):
        if stack[i] != stack[-i - 1]:
            return False
    return True


if __name__ == '__main__':
    head = SingleLinkedList.build([1, 2, 3, 3, 2, 1])
    print(str(head), palindrome(head))

    head = SingleLinkedList.build([1, 2, 3, 2, 1])
    print(str(head), palindrome(head))

    head = SingleLinkedList.build([1, 2, 3, 3, 2, 2])
    print(str(head), palindrome(head))
