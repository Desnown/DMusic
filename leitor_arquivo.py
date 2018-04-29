from os import walk
from sys import exit

class Leitor_Arquivo(object):
	def __init__(self):
		self.nome_arquivo = '5131912271920179147.txt'

		for _, _, pasta in walk('C:\\Users\\DesNown\\Desktop\\Projetos\\Email\\GUI\\'):
			if not(self.nome_arquivo,'r') in pasta:
				print("\nArquivo Não Encontrado")
				exit()
			break

	def read_lines(self):
		self.lista = []
		self.arquivo = open(self.nome_arquivo, "r")
		self.armazenar = ''

		while True:
			self.armazenar = self.arquivo.readline()
			if self.armazenar == '':
				break
			elif self.armazenar == '\n':
				continue
			else:
				self.lista.append(self.armazenar)
		self.arquivo.close()



	def adicionar(self,arg):
		self.read_lines()
		if arg in self.lista:
			pass

		else:
			self.arquivo = open("5131912271920179147.txt", "a")
			self.arquivo.write("\n%s"%arg)
		self.arquivo.close()

Leitor_Arquivo()



'''
	def number_lines(self):
		self.ler_linhas = ''

		#Variavel Global para contar as linhas
		self.cont = 0
		self.arquivo = open(self.nome_arquivo, "r")

		while True:
		#Ler cada linha
			self.ler_linhas = self.arquivo.readline()

			#Caso não tenha mais linha
			if self.ler_linhas == '' :
				break

			#Caso alguma linha estiver em branco
			elif self.ler_linhas == '\n':
				continue

			else:
				self.cont+=1

		self.arquivo.close()
'''