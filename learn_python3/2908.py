a,b = input().split()
A=list(a)
B=list(b)
A.reverse()
B.reverse()
r =[]
for i in range(3):
    if A[i]>B[i]:
        print(*A, sep='')
        break
    elif A[i]<B[i]:
        print(*B, sep='')
        break
