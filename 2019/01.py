from math import floor
mass_arr = []

with open('input01', 'r', encoding='utf-8') as fo:
    for line in fo:
        mass_arr.append(int(line))

def get_fuel_req(mass):
    return max(floor(mass / 3) - 2, 0)

print('part 1')
print(sum(map(get_fuel_req, mass_arr)))

print('part 2')
def get_fuel_req_recursive(mass):
    fuel = get_fuel_req(mass)
    if fuel == 0:
        return fuel
    return fuel + get_fuel_req_recursive(fuel)

print(sum(map(get_fuel_req_recursive, mass_arr)))
