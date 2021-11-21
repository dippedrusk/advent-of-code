with open('input02', 'r', encoding='utf-8') as f:
    xs = f.read().strip().split()

grid = [[1,2,3],
[4,5,6],
[7,8,9]
]

'''
xs = ['ULL',
'RRDDD',
'LURDL',
'UUUUD']
'''

def valid(x):
    if x >= len(grid):
        return x-1
    if x < 0:
        return 0
    return x

def n(c):
    return grid[c[0]][c[1]]

def move(c, d, mag=1):
    if d in ['L', 'R']:
        mag = mag if d == 'R' else -mag
        return (c[0], valid(c[1]+mag))
    mag = -mag if d == 'U' else mag
    return (valid(c[0]+mag), c[1])

def main(start, func):
    c = start
    ns = ''
    for x in xs:
        for d in x:
            c = func(c, d)
        ns += str(n(c))
    return ns

ns = main(start=(1,1), func=move)

print(f'part1: {ns}')

grid = [[0,0,1,0,0],
[0,2,3,4,0],
[5,6,7,8,9],
[0,'A','B','C',0],
[0,0,'D',0,0]
]

def valid2(x, y):
    assert x < len(grid) and x >= 0 and y < len(grid) and y >= 0 and n((x,y)) != 0
    return (x,y)

def move2(c, d, mag=1):
    if d in ['L', 'R']:
        mag = mag if d == 'R' else -mag
        try:
            return valid2(c[0], c[1]+mag)
        except AssertionError:
            return (c[0], c[1])
    mag = -mag if d == 'U' else mag
    try:
        return valid2(c[0]+mag, c[1])
    except AssertionError:
        return (c[0], c[1])


ns = main(start=(2,0), func=move2)
start = (2,0)

print(f'part2: {ns}')
