# Sample of for and if statement

for i in range(1, 10):
    for j in range(1, 10):
        if j >= i:
            print(i * j, end=' ')
        else:
            continue
        
        if j == 9:
            print()