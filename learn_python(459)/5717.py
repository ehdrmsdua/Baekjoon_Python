friend =[]
while True:
    M,F = map(int,input().split())
    if M == 0 and F == 0:
        break
    friend.append(M+F)

for i in range(len(friend)):
    print(friend[i])