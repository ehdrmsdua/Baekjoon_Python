n= int(input())
for _ in range(n):
    a=list(map(int,input().split()))
    a.remove(min(a))
    a.remove(max(a))
    if max(a) - min(a) >=4:
        print('KIN')
    else:
        print(sum(a))