import re

V = int(input())
who = V * r'\S'
man = input()
result = re.findall(who, man)
print(result)
if result.count('A') > result.count('B'):
    print('A')
elif result.count('A') < result.count('B'):
    print('B')
else:
    print('Tie')