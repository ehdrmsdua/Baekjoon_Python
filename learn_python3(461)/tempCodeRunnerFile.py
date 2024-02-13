T=int(input())
for _ in range(T):
    l=list(map(int,input().split()))
    del l[0]
    l.sort(reverse=True)
    print("Class",_+1)
    gap=[]
    for i in range(len(l)-1):
        gap.append(abs(l[i+1] - l[i]))
    print("Max %d, Min %d, Largest gap %d" % (l[0], l[len(l)-1],max(gap)))


