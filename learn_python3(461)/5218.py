count = int(input())
for _ in range(count):
    ans =[]
    te1, te2 = input().split(' ')
    for i in range(len(te1)):
        if ord(te2[i])>= ord(te1[i]):
            ans.append(ord(te2[i])-ord(te1[i]))
        else:
            ans.append(ord(te2[i])+26-ord(te1[i]))
    print("Distances: ", end='')
    for i in range(len(ans)):
        print(ans[i], end=' ')
    print("")