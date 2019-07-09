def exe10():
	
	zodiaco_chines = [[0, 'Macaco'], [1, 'Galo'], [2, 'Cao'], [3, 'Porco'], [4, 'Rato'], [5, 'Boi'], [6, 'Tigre'], [7, 'Coelho'], [8, 'Dragao'], [9, 'Serpente'], [10, 'Cavalo'], [11, 'Carneiro']]
	ano_nasc_familia = [1983, 1985, 2016, 2018]

	print('---Calculando o signo do zodiaco chines---')
	for membro in ano_nasc_familia:
		signo = membro % 12
		print('\nO membro com ano de nascimento {} tem o signo {}'. format(membro, zodiaco_chines[signo][1].upper()))

exe10()