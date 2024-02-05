l=[]
for _ in range(10):
    l.append(int(input()))
print(sum(l)//10)
f = {}
for i in l:
    if i in f:
        f[i] += 1
    else:
        f[i] =1
m = max(f.values())
k = [key for key, val in f.items() if val == m]
print(k[0])
