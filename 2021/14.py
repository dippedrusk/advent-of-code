from collections import Counter
from collections import defaultdict

with open('input14', 'r', encoding='utf-8') as f:
    xs = f.read().strip().split('\n\n')
    polymer, rules = xs[0], map(lambda x: x.split(' -> '), xs[1].split('\n'))
    rules = defaultdict(str, {x[0] : x[1] for x in rules})

def day14(n_steps, polymer):
    d = defaultdict(int)
    for i,j in zip(list(polymer), list(polymer)[1:]):
        d[i+j] += 1
    for _ in range(n_steps):
        t_d = defaultdict(int, {x: d[x] for x in d})
        for t in [k for k in d if d[k]]:
            t_d[t] -= d[t]
            r = rules[t]
            i,j = t[0], t[1]
            t_d[i+r] += d[t]
            t_d[r+j] += d[t]
        d = t_d
    c = Counter(polymer[-1])
    for x in d:
        c[x[0]] += d[x]
    mc = c.most_common()
    return mc[0][1] - mc[-1][1]

print(f'part1: {day14(10, polymer)}')
print(f'part2: {day14(40, polymer)}')
