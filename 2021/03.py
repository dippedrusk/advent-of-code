from collections import Counter
from collections import defaultdict

with open('input03', 'r', encoding='utf-8') as f:
    xs = f.read().strip().splitlines()

ps = defaultdict(list)

for x in xs:
    for i,c in enumerate(x):
        ps[i].append(int(c))

max_ = ''
min_ = ''

for i in ps:
    c = Counter(ps[i])
    max_ += str(max(c, key=c.get))
    min_ += str(min(c, key=c.get))

print(f'part1: {int(max_, 2) * int(min_, 2)}') # 12 mins 23 seconds

pss = []
for x in xs:
    pss.append([int(c) for c in x])

def apply_func(pss, func):
    for i in range(len(pss[0])):
        if len(pss) <= 1:
            break
        c = Counter([ps[i] for ps in pss])
        max_ = max(c, key=c.get)
        min_ = min(c, key=c.get)
        if max_ == min_:
            max_ = 1
            min_ = 0
        compare = max_ if func == 'max' else min_
        pss = [ps for ps in pss if ps[i] == compare]
    return ''.join([str(c) for c in pss[0]])

max_ = apply_func(pss, 'max')
min_ = apply_func(pss, 'min')

print(f'part2: {int(max_, 2) * int(min_, 2)}') # 34 mins 40 seconds including part 1
