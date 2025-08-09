while True:
    a,b,c = map(int, input().split())
    if a==b==c==0:
        break
    l = [a,b,c]
    l.sort()
    if l[0] == l[1] == l[2]:
        print('Equilateral')
    elif l[2] >= l[0]+l[1]:
        print('Invalid')
    elif l[0] != l[1] != l[2]:
        print('Scalene')
    else:
        print('Isosceles')
    