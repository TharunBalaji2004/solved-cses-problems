s = input().strip()
maxi = 1
count = 1

for i in range(1, len(s)):
    if (s[i] == s[i-1]):
        count += 1
    else:
        count = 1
    maxi = max(maxi, count)

print(maxi)