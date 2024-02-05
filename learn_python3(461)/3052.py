a=[]
b=[]
c={}
d=0
for _ in range(10):
    a.append(int(input()))
for i in range(10):
    b.append(a[i]%42)
for i in b:
    if i in c:
        continue
    else :
        c[i] = 1
        d=d+1
print(d)
