m=int(input())
n=int(input())
res = []
for i in range(m,n+1):
    for j in range(2,i+1):
        if j==i:
            res.append(i)
        elif i % j ==0:
            break
        else:
            continue
if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(min(res))

