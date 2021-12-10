from operator import mul
from functools import reduce

with open('input09', 'r', encoding='utf-8') as f:
    xs = [[10] + list(map(int, x)) + [10] for x in f.read().strip().splitlines()]
    xs = [[10]*len(xs[0])] + xs + [[10]*len(xs[0])]

def get_xlrud(xs, c):
    i,j = c
    x = xs[i][j]
    l = ((i,j-1), xs[i][j-1])
    r = ((i,j+1), xs[i][j+1])
    u = ((i-1,j), xs[i-1][j])
    d = ((i+1,j), xs[i+1][j])
    return x, l, r, u, d

a = []
for i in range(1,len(xs)-1):
    for j in range(1,len(xs[i])-1):
        x, l, r, u, d = get_xlrud(xs, (i,j))
        if x < l[1] and x < r[1] and x < u[1] and x < d[1]:
           a.append((i,j))

print(f'part1: {sum([xs[i][j]+1 for (i,j) in a])}')

def higher(t):
    x, l, r, u, d = get_xlrud(xs, t)
    return {y[0] for y in [l,r,u,d] if y[1] < 9 and x < y[1]}

def rec(t):
    ns = {t}
    for n in higher(t):
        ns |= rec(n)
    return ns

basins = sorted([len(rec(t)) for t in a])
print(f'part2: {reduce(mul, basins[-3:])}')
