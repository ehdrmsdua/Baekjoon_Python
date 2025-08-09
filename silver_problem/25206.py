sc=[]
sum=0.0
hsum=0.0
for _ in range(20):
    inp = input().split()
    sc.append(inp)
for i in range(len(sc)):
    if sc[i][2] == 'A+':
        h=4.5
    elif sc[i][2] == 'A0':
        h=4.0
    elif sc[i][2] == 'B+':
        h=3.5
    elif sc[i][2] == 'B0':
        h=3.0
    elif sc[i][2] == 'C+':
        h=2.5
    elif sc[i][2] == 'C0':
        h=2.0
    elif sc[i][2] == 'D+':
        h=1.5
    elif sc[i][2] == 'D0':
        h=1.0
    elif sc[i][2] == 'P':
        h=0.0
        sc[i][1] = 0
    else:
        h=0.0
    sum += h * float(sc[i][1])
    hsum += float(sc[i][1])
print(sum/hsum)