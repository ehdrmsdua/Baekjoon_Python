N =int(input())
C = []
for _ in range(N):
    x,y = map(int,input().split())
    if x == 0 or y == 0:
        C.append('AXIS')
    elif x>0 and y>0 :
        C.append('Q1')
    elif x<0 and y>0:
        C.append('Q2')
    elif x<0 and y<0:
        C.append('Q3')
    else:
        C.append('Q4')
for i in range(4):
    print('Q{}: {}'.format(i+1, C.count('Q{}'.format(i+1))))
print('AXIS: {}'.format(C.count('AXIS')))