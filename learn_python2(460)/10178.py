t=int(input())
r1=[]
r2=[]
for i in range(t):
    a,b = map(int,input().split())
    r1.append(a//b)
    r2.append(a%b)

for i in range(len(r1)):
    print(f"You get {r1[i]} piece(s) and your dad gets {r2[i]} piece(s).")