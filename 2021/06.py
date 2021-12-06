with open('input06', 'r', encoding='utf-8') as f:
    counts = [0] * 9
    xs = map(int, f.read().strip().split(','))
    for x in xs:
        counts[x] += 1

def simulate(c, n_days):
    for _ in range(n_days):
        c = [c[1], c[2], c[3], c[4], c[5], c[6], c[0]+c[7], c[8], c[0]]
    return sum(c)

print(f'part1: {simulate(counts, 80)}') # 6 minutes 36 seconds

print(f'part2: {simulate(counts, 256)}') # 47 minutes 50 seconds including part 1
# thank you Irenes!
