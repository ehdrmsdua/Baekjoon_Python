t= int(input())
tr=[]
for i in range(t):
    r=int(input())
    res = []
    C=[]
    G=[]
    for j in range(r):
        c,g = input().split()
        c=int(c)
        g=float(g)
        C.append(c)
        G.append(g)
    for j in range(r):
        res.append(G[j] * (C[j] /sum(C)))
    tr.append(sum(C)) 
    tr.append(round(sum(res),1))
for i in range(0,len(tr),2):
    print(f'{tr[i]} {tr[i+1]}')