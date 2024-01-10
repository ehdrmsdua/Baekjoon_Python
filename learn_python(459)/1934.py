from functools import reduce
T = int(input())
result = []
for i in range (T):
    A,B = map(int,input().split())
    num =[]
    for j in range(2, min(A,B)+1):
        while A%j ==0 and B%j ==0:
            A=A//j
            B=B//j
            num.append(j)
    result.append(reduce(lambda x,y: x*y, num,1)*A*B)
for i in range(len(result)):    
    print(result[i])
