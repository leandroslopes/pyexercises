from collections import Counter
import random

def exe01(lista):
	print(lista, '\n')
	print('Maior elemento: {}'.format(max(lista)))
	print('Soma total: {}'.format(sum(lista)))
	
	qtd = 0
	for n in lista:
		if (lista[0] == n):
			qtd += 1
	print('Qtd. ocorrencias 1o elem.: {}'.format(qtd))
	
	media = round(sum(lista) / len(lista), 2)
	print('Media: {}'.format(media))
	
	mais_proximo = []
	for n in lista:
		mais_proximo.append(round(abs(media - n), 2))
	print('Mais proximo da media: {}'.format(lista[mais_proximo.index(min(mais_proximo))]))
	
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

lista = random.sample(range(-20, 20), 10)
exe01(lista)