a=[]
for _ in range(5):
    a.append(int(input()))
print(min(a[0],a[1],a[2])+min(a[3],a[4])-50)