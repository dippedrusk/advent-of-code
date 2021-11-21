import hashlib

inp = 'iwrupvqb'

i = 0
while True:
    k = inp + str(i)
    h = hashlib.md5(k.encode('ascii')).hexdigest()
    if h[:6] == '000000':
        print(i, h)
        break
    i += 1

# ~11 minutes
# but i wonder if there's a cleverer way of doing this than brute force
