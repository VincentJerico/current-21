for i in range(1,6):
    for j in range(5, i-1, -1):
        print(j, end=' ')
    for k in range(i*2-2):
        print(' ', end=' ')
    for l in range(i, 6):
        if l == 5 and i == 6:
            break
        print(l, end=' ')
    print()