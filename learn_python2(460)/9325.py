t=int(input())
res=[]
for _ in range(t):
    m=0
    s=int(input())
    n=int(input())
    for i in range(n):
        q,p = map(int,input().split())
        m += q*p
    res.append(m+s)
for i in range(len(res)):
    print(res[i])