n= int(input())
l = list(map(int,input().split()))
a=max(l)
for i in range(len(l)):
    l[i] = l[i]/a*100
print(sum(l)/len(l))