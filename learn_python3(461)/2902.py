a=list(input().split('-'))
n=[]
for i in range(len(a)):
    n.append(a[i][0])
print(*n,sep='')