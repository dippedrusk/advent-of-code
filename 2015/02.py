from functools import reduce

with open('input02', 'r', encoding='utf-8') as f:
    xs = [x.split('x') for x in f.read().split()]

def area(dims):
    dims = [int(x) for x in dims]
    areas = [dims[i]*dims[i-1] for i in range(3)]
    return 2 * sum(areas) + min(areas)

def perim(dims):
    dims.remove(max(dims))
    return 2 * (dims[0] + dims[1])

def ribbon(dims):
    dims = [int(x) for x in dims]
    return reduce(lambda x,y: x*y, dims) + perim(dims)

print(sum(map(area, xs)))
print(sum(map(ribbon, xs)))

# ~10-11 mins
