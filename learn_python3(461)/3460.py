t=int(input())
for _ in range(t):
    o = []
    a=int(input())
    A=list(bin(a))
    for i in range(len(A)):
        if A[len(A)-1-i] == '1':
            o.append(i)
    print(*o)