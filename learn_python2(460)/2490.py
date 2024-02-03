for _ in range(3):
    l = list(map(int,input().split()))
    if l.count(0) == 0:
        print('E')
    elif l.count(0) ==1:
        print('A')
    elif l.count(0) ==2:
        print('B')
    elif l.count(0) ==3:
        print('C')
    else:
        print('D')