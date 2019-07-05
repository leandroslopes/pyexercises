from collections import Counter

def exe04(lista):
	
	strtam = []
	for str in lista:
		strtam.append(len(str))
	print('\nMaior string: {}'.format(lista[strtam.index(max(strtam))]))
	
	print('\nMedia de vogais por elemento')
	print('String\tQtd. Vogais\tMed. Vogais')
	lista_tam = len(lista)
	for str in lista:
		qtd_vogais = 0
		lst_str = list(str)
		for char in lst_str:
			if char in ['a', 'e', 'i', 'o', 'u']:
				qtd_vogais += 1
		print('{}\t{}\t{}'.format(str, qtd_vogais, round((qtd_vogais / lista_tam), 2)))
			
	count_ocorrencias = 0
	for str in lista:
		if (lista[0] == str):
			count_ocorrencias += 1
	print('\nQtd. ocorrencias 1o elem.: {}'.format(count_ocorrencias))
	
	count_compostas = 0
	for str in lista:
		if ' ' in str:
			count_compostas += 1
	print('\nQtd. palavras compostas: {}'.format(count_compostas))
	
	print('\nQtd. vizinhos iguais:')
	contador = Counter(lista)
	for key in contador:
		if (contador[key] > 1):
			print(key , ':', contador[key])
	
lista = ['banana', 'banana nanica', 'maca', 'maca', 'melancia', 'abacaxi de turiacu', 'mamao', 'pera', 'pera', 'abacate', 'morango', 'uva', 'melao']
exe04(lista)