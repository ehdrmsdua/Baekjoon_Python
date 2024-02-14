a,b=map(int,input().split())
c=[]
al=a-1
count=0
for _ in range(a):
    c.append(int(input()))
while b>0:
    if b >= c[al]:
        b-=c[al]
        count+=1
    else:
        al-=1
print(count)
    