t=int(input())
m=0
for i in range(t):
    a,b = map(int,input().split())
    m += b%a
print(m)