so=[]
s,e = map(int, input().split())
for i in range(s,e+1):
    k=1
    for j in range(2,i/2):
        if i % j ==0:
            k=0
            break
    if k ==1:
        so.append(i)
for i in so:
    print(i)

## 채로 다시풀기