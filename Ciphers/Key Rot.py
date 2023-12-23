def rot_ky(st, key):
    odr = []
    x = list(st.lower())
    for i in range(len(x)):
        if x[i].isalpha():
            odr.append(ord(x[i]) - 97)
        else:
            odr.append(32)
    
    ky = [ord(i) - 97 if i.isalpha() else ord(i) for i in key.lower()]
   
    ctr = 0
   
    for j in range(len(odr)):
        if odr[j] == 32:
            continue
        else:
            odr[j] = (odr[j] + ky[ctr]) % 26
            ctr = (ctr + 1) % len(ky)
            
    out = ''
    for k in range(len(odr)):
        if odr[k] == 32:
            out += ' '
        else:
            out += chr(odr[k] + 97)
    return out

a = input('Enter a string: ')
b = input('Enter Key: ')
c = rot_ky(a, b)
print(c)