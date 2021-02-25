txt = input()
for i in range(len(txt)):
    if i == len(txt)-1:
        print(1)
    elif txt[i] != txt[len(txt)-i-1]:
        print(0)
        break