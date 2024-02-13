l=[]
I=J=0
for _ in range(9):
    l.append(int(input()))
for i in range(len(l)):
    res=1
    for j in range(i+1, len(l)):
        if sum(l) - l[i] - l[j] == 100:
            I = l[i]
            J = l[j]
            res = 0
            break
    if res == 0:
        break
l.remove(I)
l.remove(J)
for i in range(len(l)):
    print(l[i])
