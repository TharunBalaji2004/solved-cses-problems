n = int(input())

if (n == 2 or n == 3):
    print("NO SOLUTION")
else:
    arr = []
    # If n is even
    if (n%2 == 0):
        num = 2
        while (num <= n):
            arr.append(num)
            num += 2
        num = 1
        while (num <= n):
            arr.append(num)
            num += 2
    else:
        # If n is odd
        num = 2
        while (num <= n-1):
            arr.append(num)
            num += 2
        num = 1
        while (num <= n):
            arr.append(num)
            num += 2
    print(" ".join(map(str, arr)))