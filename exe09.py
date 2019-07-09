def media_turma(lista):
	total_altura = 0
	
	for aluno in lista:
		total_altura += aluno[1]
		
	return round(total_altura / len(lista), 2)

def conta_baixinhos(lista, media):
	total_alunos = 0
	
	for aluno in lista:
		if aluno[0] > 13 and aluno[1] < media:
			total_alunos += 1

	print('\nQtd. de alunos com mais de 13 anos e abaixo da media da altura: {}'.format(total_alunos))

alunos = [[12, 1.29], [15, 1.34], [13, 1.21], [14, 1.41], [12, 1.15], [15, 1.32], [13, 1.19], [15, 1.3], [14, 1.22], [13, 1.41]]
media = media_turma(alunos)
conta_baixinhos(alunos, media)