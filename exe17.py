import random

def exe17(lista, lim_inf, lim_sup):
	
	print('Lista: ', lista)
	print('\nLimite inferior: ', lim_inf)
	print('Limite superior: ', lim_sup)
	
	lista_sublista = []
	for elem in lista:
		if elem >= lim_inf and elem <= lim_sup:
			lista_sublista.append(elem)
	
	print('\nSublista com os valores maiores e iguais ao limite inferior e menores e iguais ao limite superior:', lista_sublista)

lista = random.sample(range(0, 10), 7)
lim_inf = random.sample(range(0, 10), 1)
lim_sup = random.sample(range(0, 10), 1)
while lim_sup <= lim_inf:
	lim_sup = random.sample(range(0, 10), 1)

exe17(lista, lim_inf[0], lim_sup[0])