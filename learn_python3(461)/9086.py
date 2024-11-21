cas = int(input())
ans = []
for _ in range(cas):
    st = input()
    ans.append(st[0]+st[-1])
for i in range(len(ans)):
    print(ans[i])