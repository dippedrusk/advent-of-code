with open('input01', 'r', encoding='utf-8') as f:
    xs = f.read().strip().split(', ')

def turn(curr_o, direc):
    dirs = ['N', 'E', 'S', 'W']
    delta = 1 if direc == 'R' else -1
    return dirs[(dirs.index(curr_o) + delta) % len(dirs)]

def move(curr, mag, curr_o):
    if curr_o in ('N', 'S'):
        delta = mag if curr_o == 'N' else -mag
        return (curr[0], curr[1]+delta)
    delta = mag if curr_o == 'E' else -mag
    return (curr[0]+delta, curr[1])

start = (0,0)
curr = start
curr_o = 'N'
for x in xs:
    curr_o = turn(curr_o, x[0])
    curr = move(curr, int(x[1:]), curr_o)

print(f'part1: {abs(curr[0]) + abs(curr[1])}')

start = (0,0)
curr = start
curr_o = 'N'
visited = set()
for x in xs:
    done = False
    curr_o = turn(curr_o, x[0])
    for i in range(int(x[1:])):
        curr = move(curr, 1, curr_o)
        if curr in visited:
            print(f'part2: {abs(curr[0]) + abs(curr[1])}')
            done = True
            break
        visited.add(curr)
    if done:
        break
