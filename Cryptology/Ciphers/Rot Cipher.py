def rot(st, key):
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
            odr[j] = (odr[j] + key) % 26
    
    out = ''
    for k in range(len(odr)):
        if odr[k] == 32:
            out += ' '
        else:
            out += chr(odr[k] + 97)
    return out

#a = 'abcdef'
#b = 3
a = input('Enter a string: ')
b = int(input('Enter Key: '))
c = rot(a, b)
print(c)