n =int(input())
s=[0,0]
while n>0:
    if n%5 != 0:
        n -=3
        s[0]+=1
    else:
        s[1]=n//5
ans=s[0]+s[1]
if n !=0:
    ans = -1
print(ans)