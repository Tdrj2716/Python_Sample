# get the square root of x

x = 2
r_new = x/x

dif = x - r_new
if (dif < 0): dif = -dif

while (dif > 1.0E-6):
    r1 = r_new
    r2 = x/r1
    r_new = (r1 + r2)/2
    dif = r1 - r2
    print('r1:', r1, 'r_new:', r_new, 'r2:', r2)
    if (dif < 0): dif = -dif

print('the square root of ', x, 'is ', r_new)