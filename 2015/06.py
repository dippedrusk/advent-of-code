import re
from collections import defaultdict
from collections import Counter

xs = []
with open('input06', 'r', encoding='utf-8') as f:
    for x in f:
        ms = re.findall(r'(\d+),(\d+)', x)
        x_1 = int(ms[1][0])
        x_0 = int(ms[0][0])
        y_1 = int(ms[1][1])
        y_0 = int(ms[0][1])
        s = 'toggle'
        if 'on' in x:
            s = 'on'
        elif 'off' in x:
            s = 'off'
        xs.append((x_0, y_0, x_1, y_1, s))

def part1(grid):
    for x_0, y_0, x_1, y_1, s in xs:
        x_d = x_1-x_0
        y_d = y_1-y_0
        m = {0: 1, 1: 0}
        for x in range(x_0, x_0+x_d+1):
            for y in range(y_0, y_0+y_d+1):
                if s == 'on':
                    grid[(x,y)] = 1
                elif s == 'off':
                    grid[(x,y)] = 0
                else:
                    grid[(x,y)] = m[grid[(x,y)]]
    return grid

grid = defaultdict(int)
print(Counter(part1(grid).values())[1])

def part2(grid):
    for x_0, y_0, x_1, y_1, s in xs:
        x_d = x_1-x_0
        y_d = y_1-y_0
        for x in range(x_0, x_0+x_d+1):
            for y in range(y_0, y_0+y_d+1):
                if s == 'on':
                    grid[(x,y)] += 1
                elif s == 'off':
                    if grid[(x,y)] >= 1:
                        grid[(x,y)] -= 1
                else:
                    grid[(x,y)] += 2
    return grid

grid = defaultdict(int)
print(sum(part2(grid).values()))

# ~24 mins
