def exe03(lista1, lista2):
	
	print('Lista 1: {}'.format(lista1))
	print('Lista 2: {}'.format(lista2))
	
	print('\nMesmos valores e na mesma ordem: ')
	if lista1 == lista2:
		print('Listas iguais')
	else:
		print('Listas diferentes')
	
	print('\nCompostas pelos mesmos valores, mas nao obrigatoriamente na mesma ordem: ')
	for n in lista1:
		if n in lista2:
			eh_igual = True
		else:
			eh_igual = False
			break
	if eh_igual:
		print('Listas iguais')
	else:
		print('Listas diferentes')

lista1 = [3,1,2]
lista2 = [1,2,3]
exe03(lista1, lista2)