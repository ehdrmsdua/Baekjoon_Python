T=int(input())
for _ in range(T):
    l=list(map(int,input().split()))
    z=[]
    for i in range(len(l)):
        if l[i] % 2 ==0:
            z.append(l[i])
    print(sum(z), min(z))