n=int(input())
b=0
a = list(map(int,input().split()))
for i in range(len(a)):
    for j in range(2, a[i]+1):
        if a[i] == j:
            b=b+1
            break
        if a[i] % j == 0:
            break
        else:
            continue
        
print(b)      
