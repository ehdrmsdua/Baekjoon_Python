channel = int(input())
ch_list = []
method = []
for _ in range(channel):
    inpt = input()
    ch_list.append(inpt)

minus = ch_list.index('KBS2') - ch_list.index('KBS1')
if minus < 0: ## 1 in under
    for _ in range(ch_list.index('KBS1')):
        method.append(1)
    for _ in range(ch_list.index('KBS1')):
        method.append(4)
    for _ in range(ch_list.index('KBS2')+1):
        method.append(1)
    for _ in range(ch_list.index('KBS2')):
        method.append(4)
else: ## 1 in up
    for _ in range(ch_list.index('KBS1')):
        method.append(1)
    for _ in range(ch_list.index('KBS1')):
        method.append(4)
    for _ in range(ch_list.index('KBS2')):
        method.append(1)
    for _ in range(ch_list.index('KBS2')-1):
        method.append(4)
print(*method, sep ='')