s=input()
res=[0 for i in range(26)]
for i in range(len(s)):
    a= 122 - ord(s[i])
    res[len(res)-1-a] += 1
print(*res)