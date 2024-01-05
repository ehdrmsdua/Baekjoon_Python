score=[]
alphascore =[]
for i in range(0,5):
    score.append(int(input()))
alphascore = score
for i in range(0,5):
    if alphascore[i] <= 40:
        alphascore[i] = 40
print(sum(alphascore)//5)
