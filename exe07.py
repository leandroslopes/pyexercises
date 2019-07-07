from collections import Counter

def exe07():

	jogos = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]
	
	total_faltas = 0
	for i in range(0, len(jogos)):
		for j in range(0, len(jogos[i][2])):
			total_faltas += jogos[i][2][j]
	print('\nTotal de faltas do campeonato: {}'.format(total_faltas))
	
	selecoes = []
	for selecao in jogos:
		selecoes.append([selecao[0], selecao[2][0]])
		selecoes.append([selecao[1], selecao[2][1]])
	
	selecoes.sort()
	
	contabilizado = True
	nao_contabilizado = False
	for i in range(0, len(selecoes)):
		selecoes[i].append(nao_contabilizado)
	
	faltas_por_selecao = []
	for i in range(0, len(selecoes)):
		for j in range(0, len(selecoes)):
			if (i != j) and (selecoes[i][0] == selecoes[j][0]) and (selecoes[j][2] == nao_contabilizado):
				qtd_faltas = selecoes[i][1] + selecoes[j][1]
				faltas_por_selecao.append([selecoes[i][0], qtd_faltas])
				selecoes[j][2] = contabilizado
		selecoes[i][2] = contabilizado
	
	maior_falta = faltas_por_selecao[0][1]
	selecao_mais_faltosa = faltas_por_selecao[0][0]
	for selecao in faltas_por_selecao:
		if maior_falta > selecao[1]:
			continue
		else:
			maior_falta = selecao[1]
			selecao_mais_faltosa = selecao[0]
	
	selecao_mais = []
	for selecao in faltas_por_selecao:
		if selecao[1] == maior_falta:
			selecao_mais.append([selecao[0], maior_falta])
	
	menor_falta = faltas_por_selecao[0][1]
	selecao_menos_faltosa = faltas_por_selecao[0][0]
	for i in range(1, len(faltas_por_selecao)):
		if menor_falta < faltas_por_selecao[i][1]:
			continue
		else:
			menor_falta = faltas_por_selecao[i][1]
			selecao_menos_faltosa = faltas_por_selecao[i][0]
	
	selecao_menos = []
	for selecao in faltas_por_selecao:
		if selecao[1] == menor_falta:
			selecao_menos.append([selecao[0], menor_falta])

	print('\nSelecoes mais faltosas:')
	for selecao in selecao_mais:
		print('{} ({} Faltas)'.format(selecao[0], selecao[1]))
	
	print('\nSelecoes menos faltosas:')
	for selecao in selecao_menos:
		print('{} ({} Faltas)'.format(selecao[0], selecao[1]))

exe07()