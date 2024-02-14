scw=[]
scy=[]
for _ in range(10):
    scw.append(int(input()))
for _ in range(10):
    scy.append(int(input()))
scw.sort(reverse=True)
scy.sort(reverse=True)
print("{} {}".format((scw[0]+scw[1]+scw[2]),(scy[0]+scy[1]+scy[2])))
