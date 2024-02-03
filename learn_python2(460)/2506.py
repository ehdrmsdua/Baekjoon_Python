n=int(input())
sc=[0 for i in range(n)]
c=list(map(int,input().split()))
for i in range(len(c)):
    if c[i] == 1 and c[i-1] == 1 and i>0 :
        sc[i] = sc[i-1]+1
    elif c[i] ==1:
        sc[i] = 1
    elif c[i]==0:
        sc[i] =0
print(sum(sc))