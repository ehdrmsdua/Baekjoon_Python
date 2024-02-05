n= int(input())
for _ in range(n):
    a,b = input().split()
    a=int(a)
    b=list(b)
    del b[a-1]
    print(*b, sep='')