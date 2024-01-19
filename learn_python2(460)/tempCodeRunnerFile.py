import pandas as pd
n = int(input())
inform = {}
for _ in range(n):
    name, day, month, year = input().split()
    when = pd.to_datetime(year+ '-' month + '-' day)
    inform[name] =  (when) 

