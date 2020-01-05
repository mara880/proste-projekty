lista = [2, 3, 7, 4, 9]
lista2 =[]
n = 10
licznik = 1
for i in range(n):
	lista2.append(licznik)
	licznik = licznik + 1
wyjscie = [i for i in lista2 if i not in lista]
print(wyjscie)
	