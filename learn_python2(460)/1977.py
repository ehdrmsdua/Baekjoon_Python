import math
m= int(input())
l = int(input())
num = []
for i in range(int(math.sqrt(m)), int(math.sqrt(l)+1)):
    if i **2 >= m and i**2 <= l:
        num.append(i**(2))

if num:
    print(sum(num))
    print(min(num))
else:
    print(-1)