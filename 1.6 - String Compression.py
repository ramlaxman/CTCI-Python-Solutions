# Runtinme O(length(s)), since I'm using a list with amortized insert time of O(1)
# Memory O(length(s))

def compress(s):
    ret = []
    count = 0
    for i in range(len(s)):
        count += 1
        if i + 1 == len(s) or s[i] != s[i + 1]:
            ret.append(s[i] + str(count))
            count = 0

    if len(ret) * 2 < len(s):
        return ''.join(ret)
    return s

examples = [
    'abcdef',
    'aabcccccaaa',
    'abababaa'
]

if __name__ == '__main__':
    for example in examples:
        print(example, compress(example))
