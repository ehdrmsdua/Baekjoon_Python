n=int(input())
res=[]
for i in range(n):
    res.append(int(input()))
print(sum(res)- (n-1))