s,e = map(int,input().split())
n=[]
for i in range(e+1):
    for j in range(i):
        n.append(i)
print(n)
print(sum(n[s-1:e]))
