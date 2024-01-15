S = []
P = []
while True:
    T = list(map(int,input().split()))
    if T == [0,0]:
        break
    else:
        S.append(T)
for i in range(len(S)):
    if S[i][1] % S[i][0] == 0:
        P.append('factor')
    elif S[i][0] % S[i][1] == 0:
        P.append('multiple')
    else: 
        P.append('neither')

for i in range(len(P)):
    print(P[i])