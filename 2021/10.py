with open('input10', 'r', encoding='utf-8') as f:
    xs = f.read().strip().splitlines()

m = {'(': ')', '[': ']', '{': '}', '<': '>'}
d = {')': 3, ']': 57, '}': 1197, '>': 25137}

def p1(x):
    s, a = 0, []
    for t in x:
        if t in m:
            a.append(t)
        elif t in d:
            p = a.pop()
            if m[p] != t:
                s += d[t]
                break
    return s, a

score = 0
lines = []
for x in xs:
    s, a = p1(x)
    score += s
    if not s:
        lines.append(a)

print(f'part1: {score}') # 27 mins 11 seconds

d = {')': 1, ']': 2, '}': 3, '>': 4}

score = []
for a in lines:
    s, l = 0, len(a)
    while l:
        p = a.pop()
        s, l = s*5 + d[m[p]], len(a)
    score.append(s)

print(f'part2: {sorted(score)[len(score)//2]}') # 35 mins 24 seconds including part 1
