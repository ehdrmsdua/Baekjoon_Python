T = int(input())
for i in range(T):
  x = 0
  y = 0
  T2 = int(input())
  for j in range(T2):
    n, m = map(float, input().split())
    x += n
    y += (n*m)
  print("%d %.1f"%(x,y/x))