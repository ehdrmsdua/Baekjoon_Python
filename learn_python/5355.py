T = int(input())
for i in range(T):
    a=list(input().split())
    answer= float(a[0])
    for i in range(1,len(a)):
        if a[i] == '@':
            answer *=3
        elif a[i] == '%':
            answer +=5
        elif a[i] == '#':
            answer -=7
    print('{:.2f}'.format(answer))
        