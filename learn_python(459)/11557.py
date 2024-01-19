T = int(input())
re = []
for _ in range(T):
    N = int(input())
    SL = [] 
    LL= []
    for i in range(N):
        S, L = input().split()
        L = int(L)
        SL.append(S)
        LL.append(L)
    M = LL.index(max(LL))
    re.append(SL[M])
for j in range(T):
    print(re[j])