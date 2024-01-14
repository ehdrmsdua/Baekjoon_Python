N = int(input())
a = []
for i in range(N):
    r,e,c = map(int, input().split())
    if r> e-c:
        a.append('do not advertise')
    elif r == e-c:
        a.append('does not matter')
    else:
        a.append('advertise')
for i in range(N):
    print(a[i])
