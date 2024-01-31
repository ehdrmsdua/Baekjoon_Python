from functools import reduce
a=list(map(int,input().split()))
print(sum(map(lambda x: x ** 2 ,a))%10)
