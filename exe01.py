from collections import Counter

def exe01(lista):
	print('Maior elemento: {}'.format(max(lista)))
	print('Soma total: {}'.format(sum(lista)))
	
	qtd = 0
	for n in lista:
		if (lista[0] == n):
			qtd += 1
	print('Qtd. ocorrencias 1o elem.: {}'.format(qtd))
	
	print('Media: {}'.format(sum(lista) / len(lista)))
	print('Mais proximo da media: {}'.format(0))
	
	total_negativos = 0
	for n in lista:
		if (n < 0):
			total_negativos += n
	print('Soma dos negativos: {}'.format(total_negativos))

	contador = Counter(lista)
	print('Qtd. vizinhos iguais:')
	for key in contador:
		if (contador[key] > 1):
			print(key , ':', contador[key])

lista = [-4, -1, -3, -3, 0, 1, 1, 1, 2, 4, 7, 7, 8, 9, 12, -13, -17]	
exe01(lista)