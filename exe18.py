import random

def exe18(lista):
	
	pri_met = []
	seg_met = []
	meio_lista = int(len(lista)/2)
	tam_lista = len(lista)
	
	for i in range(meio_lista, tam_lista):
		seg_met.append(lista[i])
		
	for i in range(0, meio_lista):
		pri_met.append(lista[i])
	
	print('Lista:', lista)
	print('Ultima metade da lista:', seg_met)
	print('Primeira metade da lista:', pri_met)
	
lista = random.sample(range(0, 10), 8)	
exe18(lista)