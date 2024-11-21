n = int(input())
num=1
for i in range(1, n+1):
    num *= i
num = list(str(num))
count=0
for i in range(len(num)-1,0,-1):
    if num[i] == '0':
        count+=1
    else:
        break
print(count)