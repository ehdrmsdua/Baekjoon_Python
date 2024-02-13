word = list(input())
l=[]
alpha = [chr(i) for i in range(97,123)]
for i in range(len(alpha)):
        if alpha[i] in word:
            l.append(word.index(alpha[i]))
        else:
            l.append(-1)
print(*l)