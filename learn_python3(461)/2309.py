a=[]
for _ in range(9):
    a.append(int(input()))
f=False
for i in range(9):
    if f:
        break
    for j in range(i+1, 9):
        if sum(a) - (a[i]+a[j]) == 100:
            o=a[i]
            t=a[j]
            a.remove(o), a.remove(t)
            f = True
            break
a.sort()
print(*a,sep='\n')