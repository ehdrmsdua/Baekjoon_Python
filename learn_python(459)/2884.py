H,M = map(int,input().split())
def clock(H, M):
    if M >= 45:
        M = M-45
        print(H,M)
    elif M < 45:
        M = 60 + (M-45)
        if H == 0:
            H = 23
        else: 
            H = H-1
        print(H,M)
clock(H, M)
