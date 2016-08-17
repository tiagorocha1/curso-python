def gera_nome_convite(convite):
	tamanho=len(convite)
	parte1 = convite[0:4]
	parte2 = convite[tamanho-4:tamanho]
	return parte1 +" "+parte2

def envia_convite(nome_formatado):
	print 'Enviando convite para %s' % (nome_formatado)

def processa_convite(convite):
	nome_formatado=gera_nome_convite(convite)
	envia_convite(nome_formatado)