n= int(input())
num=1
k=1
while True:
   num += 6*k
   k+=1
   if n <= num:
      break
print(k)