with open('input01', 'r', encoding='utf-8') as f:
    xs = [x for x in f.read().strip()]

m = {'(': 1, ')': -1}

print(sum([m[x] for x in xs]))

s = 0
for i,x in enumerate(xs):
    s += m[x]
    if s == -1:
        print(i+1)
        break

# ~4-5 minutes
