t=int(input())
n =[]
for _ in range(t):
    n.append(int(input()))
n.sort()
for i in range(t):
    print(n[i])