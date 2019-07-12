import random

def exe11(lista):
	
	lista_aux = sorted(lista)
	
	print('Lista parametro: ', lista)
	print('Lista ordenada: ', lista_aux)
	
	if lista == lista_aux:
		print('\nLista ordenada!')
	else:
		print('\nLista nao ordenada!')

lista = random.sample(range(0, 10), 10)
exe11(lista)