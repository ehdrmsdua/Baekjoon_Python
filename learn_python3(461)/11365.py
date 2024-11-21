text= []
while True:
    t = input()
    if t == 'END':
        break
    text.append(t)
    for i in range(len(text)):
        text_a =[]
        for j in range(len(text[i])):
            text_a.append(text[i][len(text[i])-1-j])
        for k in range(len(text_a)):
            print(text_a[k],end='')
        print('')
        text.clear()