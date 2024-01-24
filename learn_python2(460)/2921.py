n=int(input())
a=[]
b=[]
for i in range(n+1):
    a.append(i)
    for j in range(n+1):
        if a[i]<=j:
            b.extend([i,j])
print(sum(b))