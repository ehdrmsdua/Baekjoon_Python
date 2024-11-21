word = input("")
word = list(word.upper())
count = {}
for i in range(len(word)):
    if word[i] in count.keys():
        count[word[i]] += 1
    else :
        count[word[i]] = 1
ans = 0
ans2 = 'a'
for i in count.keys():
    if count[i] > ans:
        ans = count[i]
        ans2 = i
    else:
        continue
if list(count.values()).count(max(count.values())) != 1:
    ans2 = '?'
print(ans2)