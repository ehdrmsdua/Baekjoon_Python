a,b = map(int, input().split())
res=[]
c=list(map(int,input().split()))
for i in range(len(c)):
    if b>c[i]:
        res.append(c[i])
print(*res)
    

