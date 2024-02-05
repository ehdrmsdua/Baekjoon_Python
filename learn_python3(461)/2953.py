a=[]
m=-1
mm=0
for _ in range(5):
    a.append(list(map(int,input().split())))
for i in range(5):
    if m < sum(a[i]):
        m=sum(a[i])
        mm=i+1
print(mm, m)