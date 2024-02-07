t=int(input())
for _ in range(t):
    l = int(input())
    a= list(map(int,input().split()))
    a.sort()
    min1= 999
    for i in range(max(a)+1):
        s=0
        for j in range(l):
           if j == 0:
               s=abs(a[j]-i)
           else:
               s += abs(a[j]-a[j-1])
        if s<min1:
            min1=s
    print(s)

