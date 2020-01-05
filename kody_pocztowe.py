a = '79-900'
b = "80-155"
a1 = a[:2]
a2 = a[3:]
kod_min = int(a1+a2)
b1 = b[:2]
b2 = b[3:]
kod_max = int(b1+b2)
while kod_min < kod_max:
	kod_min = kod_min + 1
	kody = str(kod_min)
	print(kody[:2],"-",kody[2:])