def aff(st, keya, keyb):
    odr = []
    x = list(st.lower())
    for i in range(len(x)):
        if x[i].isalpha():
            odr.append(ord(x[i]) - 97)
        else:
            odr.append(32)
    
    for j in range(len(odr)):
        if odr[j] == 32:
            continue
        else:
            odr[j] = ((keya * odr[j]) + keyb) % 26

    out = ''
    for k in range(len(odr)):
        if odr[k] == 32:
            out += ' '
        else:
            out += chr(odr[k] + 97)
    return out

#a = 'abcDEF ghi'
#b, c = 1, 2
a = input('Enter a string: ')
b, c = map(int,input('Enter Key: ').split())
d = aff(a, b, c)
print(d)