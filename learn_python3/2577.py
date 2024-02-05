a=1
l=[]
for _ in range(3):
    a= a* int(input())
a=str(a)
a=list(a)
for i in range(10):
        print(a.count(str(i)))