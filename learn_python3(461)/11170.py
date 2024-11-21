case = int(input())
for _ in range(case):
    st,en = input().split(' ')
    li =[]
    st = int(st)
    en = int(en)
    for i in range(st,en+1):
        while True:
            li.append(i%10)
            if i-10 <0:
                break
            i = i//10
    print(li.count(0))
    li.clear()