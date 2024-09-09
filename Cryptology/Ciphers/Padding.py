def pad(st, num):
    for i in range(num - len(st)):
        a.append('\\x01')

    for j in st:
        print(j, end='')

a = list(input('Enter The String: '))
b = int(input('Enter the Number of Bytes: '))

pad(a,b)