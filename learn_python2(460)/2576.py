l= []
h=[]
for _ in range(7):
    l.append(int(input()))
for i in range(7):
    if l[i] % 2 == 0:
        continue
    elif l[i] % 2 != 0:
        h.append(l[i])

if len(h)>0:
    print(sum(h))
    print(min(h))
else: print(-1)
