res = []
while True:
    n = int(input())
    if n == -1:
        break
    w=[]
    T=0
    for i in range(1, n):
        if n % i == 0:
            w.append(i)
    for j in range(len(w)):
        T = T+w[j]
    if T == n:
        res.append(f'{T} = ' + ' + '.join(map(str,w)))
    else: 
        res.append(f'{n} is NOT perfect.')
    
for i in res:
    print(i)
