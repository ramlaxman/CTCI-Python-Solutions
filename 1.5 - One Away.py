
def one_away(s1, s2):
    if len(s1) == len(s2):
        same = True
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if not same:
                    return False
                same = False
        return True

    if len(s1) > len(s2):
        s1, s2 = s2, s1

    if len(s2) - len(s1) > 1:
        return False

    inserted = 0
    for i in range(len(s1)):
        if s1[i] != s2[i + inserted]:
            if inserted:
                return False
            inserted = 1
    return True

examples = [
    ('pale', 'ple'),
    ('pales', 'pale'),
    ('pale', 'bale'),
    ('pale', 'bake'),
    ('pales', 'pal'),
    ('', 'a'),
    ('ab', ''),
    ('a', 'a')
]

if __name__ == '__main__':
    for s1, s2 in examples:
        print(s1 or "''", s2 or "''", one_away(s1, s2))
