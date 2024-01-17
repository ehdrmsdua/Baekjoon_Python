T = int(input())
A = 0
B = 0
C =0
while True:
    if T - 300 >= 0:
        T = T-300
        A = A+1
    elif T - 60 >= 0:
        T = T-60
        B = B+1
    elif T - 10 >=0:
        T = T-10
        C = C+1
    elif T > 0 and T <10:
        print(-1)
        break
    elif T == 0:
        print(f'{A} {B} {C}')
        break