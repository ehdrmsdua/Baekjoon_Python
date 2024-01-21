n = list(map(int,input().split(':')))
s = list(map(int,input().split(':')))
l = []
for i in range(3):
    if (n[i]-s[i]) <= 0 :
        l.append(s[i] - n[i])
    elif n[i] > s[i] and i !=0 :
        l.append(60-(n[i]-s[i]))
        if l[i-1] - 1>=0:
            l[i-1]=l[i-1] -1
        elif l[i-1] - 1<0 and l[i-2] -1<0 and i ==2:
            l[i-2] = 23
            l[i-1] = 59
        elif l[i-1] - 1<0 and l[i-2] -1>=0 and i ==2:
            l[i-2] = l[i-2] -1
            l[i-1] = 59
        elif l[i-1] - 1<0 and i ==1:
            l[i-1] = 23
    elif n[0] > s[0] :
        l.append(24-(n[0]-s[0]))
print('%02d:%02d:%02d'%(l[0],l[1],l[2]))