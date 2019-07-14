import random

def exe15(notas):
	
	maior_nota = max(notas)
	
	print('\nNota Antiga - Nova Nota')
	for nota in notas:
		print(nota, '\t\t', round(nota*10/maior_nota, 1))
	
notas = random.sample(range(1, 7), 5)
exe15(notas)