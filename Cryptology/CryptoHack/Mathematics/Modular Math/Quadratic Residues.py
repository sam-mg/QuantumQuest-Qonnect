for i in range(1, 1000):
	a=[]
	if (i ** 2) % 29 == 14:
		a. append(i)
		break
	if (i ** 2) % 29 == 6:
		a. append(i)
		break
	if (i ** 2) % 29 == 11:
		a. append(i)
		break
print(min(a))