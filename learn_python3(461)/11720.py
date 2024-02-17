input()
a=list(input())
sum=0
for i in range(len(a)):
    a[i] = int(a[i])
    sum+=a[i]
print(sum)