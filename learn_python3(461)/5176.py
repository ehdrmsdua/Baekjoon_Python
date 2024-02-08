k = int(input())

for _ in range(k):
    p,n = map(int,input().split())
    a=[]
    for _ in range(p):
        a.append(int(input()))
    count = 0
    for i in range(len(a)-1):
        a.sort()
        if a[i] == a[i+1]:
            count +=1
    print(count)
    