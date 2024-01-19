n = int(input())
result= []
for _ in range(n):
    dic = {}
    p= int(input())
    for i in range(p):
        c,n = input().split()
        c = int(c)
        dic[c] = n
    result.append(dic[max(dic)])
for i in range(len(result)):
    print(result[i])
