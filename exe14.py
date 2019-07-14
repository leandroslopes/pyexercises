import random

def exe14(megasena_resultado, jogadores):

	print('Resutado da megasena:', megasena_resultado)
	
	ganhadores = []
	for jogador in jogadores:
		if jogador[1] == megasena_resultado:
			ganhadores.append(jogador[0])
	
	print('\nGanhadores:')
	if len(ganhadores) == 0:
		print('Nao houve ganhadores')
	else:
		for ganhador in ganhadores:
			print(ganhador)
	
def criar_lista_jogadores():
	
	jogadores = []
	
	digito = 1
	for i in range(0, 9):
		cpf = ''
		for j in range(0, 11):
			cpf += str(digito)
		aposta = random.sample(range(1, 60), 6)
		aposta.sort()
		jogadores.append([cpf, aposta])
		digito += 1
	
	return jogadores

megasena_resultado = random.sample(range(1, 60), 6)
megasena_resultado.sort()
jogadores = criar_lista_jogadores()
exe14(megasena_resultado, jogadores)