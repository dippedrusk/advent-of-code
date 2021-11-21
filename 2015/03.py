with open('input03', 'r', encoding='utf-8') as f:
    xs = [x for x in f.read()]

s = (0,0)
m = {'^': (1,0), 'v': (-1,0), '>': (0,1), '<': (0,-1)}

def santa(xs, s=s):
    visited = set()
    n = s
    for x in xs:
        visited.add(n)
        c = m[x]
        n = (n[0]+c[0], n[1]+c[1])
    return visited

s_xs = [x for i,x in enumerate(xs) if i % 2 == 0]
r_xs = [x for i,x in enumerate(xs) if i % 2 == 1]

print(len(santa(s_xs) | santa(r_xs)))

# ~7 minutes
