man = 0
maxman = 0
on = 0
off = 0
for _ in range(10):
    off, on = map(int,input().split())
    man = man-off+on
    if maxman<man:
        maxman = man
print(maxman)