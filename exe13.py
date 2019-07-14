import random

def exe13(lista1, lista2):
	
	print('Lista 1:', lista1)
	print('Lista 2:', lista2)
	
	lista_intersecao = [i for i in lista1 if i in lista2]
	lista_uniao = list({i: i for i in lista1 + lista2}.values())

	index = 1
	lista_intercalacao = lista1
	for elem2 in lista2:
		lista_intercalacao.insert(index, elem2)
		index += 2

	print('\nLista intersecao:', lista_intersecao)
	print('Lista uniao:', lista_uniao)
	print('Lista intercalada:',lista_intercalacao)
	
lista1 = random.sample(range(0, 10), 5)
lista2 = random.sample(range(0, 10), 5)
exe13(lista1, lista2)