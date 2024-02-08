n = int(input())
a=[]
for _ in range(n):
    b = int(input())
    if b == 0 :
        del a[len(a)-1]
    else: a.append(b)
print(sum(a))