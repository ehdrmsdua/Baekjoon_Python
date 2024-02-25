import math
a=input()
for i in range(math.ceil(len(a)/10)):
    b=(a[10*i:(i+1)*10])
    print(*b,sep='')