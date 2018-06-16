def is_substring(s1, s2):
    return s1 in s2 # O(len(s2))

# Runtime: O(len(s2))
# Memory: O(len(s2))
def is_rotation(s1, s2):
    s2 = s2 + s2 # Runtime: O(len(s2)) Memory: O(len(s2))
    return is_substring(s1, s2)

if __name__ == '__main__':
    s1 = 'waterbottle'
    s2 = 'erbottlewat'
    print(is_rotation(s1, s2))
    s1 = 'notarotation'
    s2 = 'anotrotation'
    print(is_rotation(s1, s2))
