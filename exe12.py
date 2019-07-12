import random

def exe12(lista, valor):
	
	retorno = 0
	
	print('Lista:', lista)
	print('Valor a ser buscado:', valor)
	
	if len(lista) == 0:
		retorno = -2
	elif valor in lista:
		retorno = lista.index(valor)
	else:
		retorno = -1
		
	if retorno == -1:
		print('\nCodigo {} -> O valor {} nao estah na lista'.format(retorno, valor))
	elif retorno == -2:
		print('\nCodigo {} -> Lista estah vazia'.format(retorno))
	else:
		print('\nPosicao do valor {}: {}'.format(valor, retorno))
	
lista = random.sample(range(0, 10), 10)
valor = random.randrange(20)
exe12(lista, valor)