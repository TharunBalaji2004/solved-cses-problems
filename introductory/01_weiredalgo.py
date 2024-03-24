n = int(input())

while (True):
    if (n%2 == 0):
        if (n == 1):
            print(1)
            break
        print(n, end=' ')
        n = n//2
    else:
        if (n == 1):
            print(1)
            break
        print(n, end=' ')
        n = 3*n + 1
        
        
    