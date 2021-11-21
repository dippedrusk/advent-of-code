with open('input02', 'r', encoding='utf-8') as fo:
    integers_raw = list(map(int, fo.read().strip().split(',')))

def run_computer(integers):
    for i in range(0, len(integers)-(len(integers)%4), 4):
        if integers[i] == 1:
            integers[integers[i+3]] = integers[integers[i+2]] + integers[integers[i+1]]
        elif integers[i] == 2:
            integers[integers[i+3]] = integers[integers[i+2]] * integers[integers[i+1]]
        elif integers[i] == 99:
            break
        else:
            print(f'something broke at {i}: {integers[i]}')
    return integers

def get_output(integers):
    return integers[0]

print('part 1')
integers = [n for n in integers_raw]
integers[1] = 12
integers[2] = 2
integers_new = run_computer(integers)
print(get_output(integers_new))

print('part 2')
for x in range(0, 100):
    for y in range(0, 100):
        integers = [n for n in integers_raw]
        #print(integers_raw)
        integers[1] = x
        integers[2] = y
        try:
            integers = run_computer(integers)
        except IndexError:
            continue
        if get_output(integers) == 19690720:
            print(100*x+ y)
            break
