man = 0
maxman=0
for _ in range(4):
    l= list(map(int,input().split()))
    man = man + l[1]-l[0]
    if man > maxman:
        maxman = man
print(maxman)