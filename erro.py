from models import *
arquivo = None
perfis = [] 
try:
	arquivo = open('perfis.csv','r')
	print('arquivo foi aberto')
	for linha in arquivo:
		valores = linha.split(',')
		perfis.append(Perfil(*valores))	
except (IOError,TypeError) as error:
	print('Deu erro %s' %error)
finally:
	if(arquivo is not None):
		print("Fechando o arquivo")		
		arquivo.close()
	if(perfis is not None):
		print('Perfis criados:')
		for p in perfis:
			p.imprimir()
