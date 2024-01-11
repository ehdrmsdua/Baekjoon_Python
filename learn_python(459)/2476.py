N=int(input())
win = []
for i in range(N):
    A,B,C = map(int,input().split())
    if A == B == C:
        win.append(10000+A*1000)
    elif A == B:
        win.append(1000+A*100)
    elif A == C:
        win.append(1000+A*100)
    elif B == C:
        win.append(1000+B*100)
    else:
        win.append(max(A,B,C)*100)

print(max(win))