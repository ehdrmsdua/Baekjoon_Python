s=list(map(float,input().split(',')))
count=0
for i in range(len(s)):
    if s[i]%1 ==0:
        count+=1
print(count)