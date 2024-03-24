n = int(input())
total = (n*(n+1))//2

if (total%2 == 0):
    arr1, arr2 = [], []
    visited = [0]*(n+1)
    
    sum1 = 0
    maxi = n
    
    while (sum1 < total//2):
        rem = total//2 - sum1
        
        if (rem > maxi):
            arr1.append(maxi)
            visited[maxi] = 1
            sum1 += maxi
            maxi -= 1
        else:
            arr1.append(rem)
            visited[rem] = 1
            sum1 = total//2
    
    for i in range(1, n+1):
        if (visited[i] == 0):
            arr2.append(i)
            
    print("YES")
    print(len(arr1))
    print(" ".join(map(str, arr1)))
    print(len(arr2))
    print(" ".join(map(str, arr2)))
else:
    print("NO")