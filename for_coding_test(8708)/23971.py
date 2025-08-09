h,w,n,m = map(int,input().split())
num = 0
while w > 0:
    num +=1
    w -= m+1
x= num
while h > 0 :
    num +=x
    h -= n+1
num -= x
print(num)