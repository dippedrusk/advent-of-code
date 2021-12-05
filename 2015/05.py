with open('input05', 'r', encoding='utf-8') as f:
    xs = f.read().strip().split()

def good(x):
    for y in ['ab', 'cd', 'pq', 'xy']:
        if y in x:
            return False
    v_c = 0
    for y in 'aeiou':
        v_c += x.count(y)
    if v_c < 3:
        return False
    for y,z in zip(x[:],x[1:]):
        if y == z:
            return True
    return False

print(list(map(good, xs)).count(True))

def good2(x):
    g = False
    for y,z,a in zip(x[:], x[1:], x[2:]):
        if y == a:
            g = True
    if not g:
        return False
    d = {}
    for i,(y,z) in enumerate(zip(x[:],x[1:])):
        d[i] = (y,z)
    # pylint: disable=consider-using-dict-items
    for i in d:
        for j in range(i+2,len(x)-1):
            if d[j] == d[i]:
                return True
    return False

print(list(map(good2, xs)).count(True))

# woof, ~22 mins
