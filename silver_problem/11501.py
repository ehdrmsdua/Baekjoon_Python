import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(input())
    price = list(map(int,(sys.stdin.readline().strip().split())))
    revenue = 0
    for i in range(len(price)):
        x = max(price[i:])
        if price[i] >= x:
            continue
        else:
            revenue += x-price[i]
    print(revenue)
