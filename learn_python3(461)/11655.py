text = input()
text_a = []
for i in range(len(text)):
    if ord(text[i])>=65 and ord(text[i])<=90:
        if ord(text[i])+13 > 90:
            text_a.append(chr(64+(13-(90-ord(text[i])))))
        else:
            text_a.append(chr(ord(text[i])+13))
    elif ord(text[i])>=97 and ord(text[i])<=122:
        if ord(text[i])+13 > 122:
            text_a.append(chr(96+(13-(122-ord(text[i])))))
        else:
            text_a.append(chr(ord(text[i])+13))
    else:
        text_a.append(text[i])
print(*text_a,sep='')