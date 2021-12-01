with open('input01', 'r', encoding='utf-8') as f:
    xs = f.read().strip().splitlines()

"""
xs = '''199
200
208
210
200
207
240
269
260
263
'''.splitlines()
"""

xs = [int(x) for x in xs]

count = 0
for (x,y) in zip(xs, xs[1:]):
    if y > x:
        count += 1

print(f'part1: {count}')

count = 0
for i, (a,b,c) in enumerate(zip(xs[1:], xs[2:], xs[3:])):
    x, y, z = xs[i], xs[i+1], xs[i+2]
    if sum([int(a),int(b),int(c)]) > sum([int(x),int(y),int(z)]):
        count += 1

print(f'part2: {count}')

# ~ 8 mins
