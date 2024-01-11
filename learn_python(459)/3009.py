a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
c1,c2 = map(int,input().split())
if a1 == b1 and a2 != c2:
    d1 = c1
    d2 = a2
elif a1 == b1 and a2 == c2:
    d1 = c1
    d2 = b2
elif a1 == c1 and a2 != b2:
    d1 = b1
    d2 = a2
elif a1 == c1 and a2 == b2:
    d1 = b1
    d2 = c2
elif b1 == c1 and b2 != a2:
    d1 = a1
    d2 = b2
elif b1 == c1 and b2 == a2:
    d1 = a1
    d2 = c2
print(d1,d2)