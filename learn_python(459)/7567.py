G = list(input())
num = 10
for i in range(len(G)-1):
    if G[i] != G[i+1]:
        num = num+10
    else :
        num = num+5
print(num)