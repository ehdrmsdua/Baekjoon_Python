a,b = input().split()
a=list(a); b=list(b)
A=0; B=0
a.reverse(); b.reverse()
for i in range(len(a)):
    A += int(a[i]) * (10**(len(a)-1-i))
for i in range(len(b)):
    B += int(b[i]) * (10**(len(b)-1-i))
rs=A+B ; rs=str(rs); rs=list(rs)
rs.reverse()
irs=0
for i in range(len(rs)):
    irs += int(rs[i]) * (10**(len(rs)-1-i))
print(irs)