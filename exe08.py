def exe08(lista):
	
	media = round(sum(lista) / len(lista), 2)
	print('\nMedia: {}'.format(media))
	
	mais_proximo = []
	for n in lista:
		mais_proximo.append(round(abs(media - n), 2))
	print('Mais proximo da media: {}'.format(lista[mais_proximo.index(min(mais_proximo))]))

lista = [2.5, 7.5, 10.0, 4.0]
exe08(lista)