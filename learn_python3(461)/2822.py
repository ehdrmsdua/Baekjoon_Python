sc=[]
an = []
for _ in range(8):
    sc.append(int(input()))
scs = sorted(sc, reverse= True)
print(sum(scs[0:5]))
for i in range(5):
    an.append(sc.index(scs[i])+1)
an.sort()
print(*an)