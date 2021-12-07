with open('input07', 'r', encoding='utf-8') as f:
    xs = list(map(int, f.read().strip().split(',')))

def cost(n, cumsum=False):
    return n * (n+1) // 2 if cumsum else n

def get_distance(crabs, cumsum=False):
    counts = []
    for i in range(1, max(crabs)//2):
        counts.append(sum([cost(abs(c-i), cumsum) for c in crabs]))
    return counts

print(f'part1: {min(get_distance(xs))}') # 3 mins 31 seconds

print(f'part2: {min(get_distance(xs, cumsum=True))}') # 30 mins 37 seconds including part 1
