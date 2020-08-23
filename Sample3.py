# get the square root of x by using while and if statement
while True:
    i = input('x is: ')
    try:
        x = float(i)
    except ValueError:
        print(i, 'cannot be converted into a number')
        continue
    except:
        print('This error is unexpected')
        exit()
    if (x <= 0):
        print(x, 'is not positive')
        continue
    else:
        break

r_new = x

while True:
    r1 = r_new
    r2 = x/r1
    r_new = (r1 + r2)/2
    dif = r1 - r2
    print('r1:', r1, 'r_new:', r_new, 'r2:', r2)

    if (dif < 0): dif = -dif
    if (dif <= 1.0E-6): break

print('the square root of ', x, 'is ', r_new)