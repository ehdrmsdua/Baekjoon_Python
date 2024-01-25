n,k = map(int,input().split())
y=[]
for i in range(1,n+1):
    if n%i ==0:
        y.append(i)

if k <= len(y):
    print(y[k-1])
else:
    print(0)