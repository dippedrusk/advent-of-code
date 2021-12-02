with open('input02', 'r', encoding='utf-8') as f:
    xs = f.read().strip().splitlines()

def move(c, d, mag):
    if d in ['forward']:
        return (c[0], (c[1]+mag))
    mag = -mag if d == 'up' else mag
    return ((c[0]+mag), c[1])

def main(start, func):
    c = start
    for x in xs:
        d,m = x.split()
        c = move(c, d, int(m))
    return c[0] * c[1]

print(f'part1: {main((0,0), move)}') # 8 mins 59 seconds

def move(c, d, mag):
    if d in ['forward']:
        return (c[0] + c[2]*mag, (c[1]+mag), c[2])
    mag = -mag if d == 'up' else mag
    return (c[0], c[1], c[2]+mag)

print(f'part2: {main((0,0,0), move)}') # 11 mins 37 seconds (including part 1)
