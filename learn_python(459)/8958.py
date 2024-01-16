N = int(input())
tt = []
for _ in range(N):
    sc= []
    re = list(input())
    for k in range(len(re)):
        sc.append(0)
    if re[0] == 'O':
        sc[0]= 1
    else:
        sc[0]=0
    for i in range(len(re)-1):
        if re[i+1] == 'O':
            if re[i] == 'O':
                sc[i+1] = sc[i]+1
            else: 
                sc[i+1] = 1
        elif re[i+1] == 'X':
            sc[i+1] = 0 
    tt.append(sum(sc))
for i in range(len(tt)):
    print(tt[i])