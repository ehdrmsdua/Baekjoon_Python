n = int(input())
A = 100
B = 100
for i in range(n):
    r1, r2 = map(int,input().split())
    if r1 > r2:
        B = B - r1
    elif r1 < r2:
        A = A - r2
print(A, B, sep = '\n')