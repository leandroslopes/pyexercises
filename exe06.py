def exe06(mensagem):
	
	codigos = list(' abcdefghijklmnopqrstvwxyz')
	
	msg = ''
	for i in mensagem:
		msg += codigos[i]
	print(msg)

msg_secreta = [2,15,13,0,4,9,1]
exe06(msg_secreta)