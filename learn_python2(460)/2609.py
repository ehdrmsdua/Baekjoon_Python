num1, num2 = map(int, input().split())
y=[]
for i in range(1, min(num1,num2)+1):
    if num1 % i ==0 and num2 % i == 0:
        y= i
print(y)
print(int(num1 *(num2/y)))