from collections import Counter

with open('input05', 'r', encoding='utf-8') as f:
    xs = f.read().strip().splitlines()


def step(x1, y1, x2, y2, allow_diagonals=False):
    if not allow_diagonals and not (x1 == x2 or y1 == y2):
        return
    x_mag, y_mag = 0, 0
    if x1 != x2:
        x_mag = 1 if x2 > x1 else -1
    if y1 != y2:
        y_mag = 1 if y2 > y1 else -1
    x, y = x1, y1
    while not (x == x2+x_mag and y == y2+y_mag):
        yield (x,y)
        x += x_mag
        y += y_mag

coords = Counter()
diag_coords = Counter()

for x in xs:
    l, r = x.split(' -> ')
    x1, y1 = map(int, l.split(','))
    x2, y2 = map(int, r.split(','))
    for _x, _y in step(x1, y1, x2, y2):
        coords[(_x,_y)] += 1
    for _x, _y in step(x1, y1, x2, y2, allow_diagonals=True):
        diag_coords[(_x,_y)] += 1

print(f'part1: {len([c for c in coords if coords[c] > 1])}') # 21 mins 47 seconds

print(f'part2: {len([c for c in diag_coords if diag_coords[c] > 1])}') # 35 mins 02 seconds including part 1
