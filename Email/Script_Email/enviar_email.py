import smtplib, socket
from time import sleep
from getpass import getpass

class SendEmail():
	def __init__(self):
		while True:
			try:
				#Criando um Objeto
				self.smtp_obj = smtplib.SMTP("smtp.gmail.com",587)
				#self.hot_obj = smtplib.SMTP("smtp-mail.outlook.com", 587)
				break

			#Se não estiver conectado a internet, o python irá levantar um erro(socket.gaierror)
			except socket.gaierror:
				print("Você não está conectado na internet...")

			sleep(5)

		while True:
			#Estabelecendo uma conexão com o servidor
			self.conexao = self.smtp_obj.ehlo()

			#Verificando se a conexão deu certo
			if 250 in self.conexao:
				break

			else:
				print("Conexão Não Estabelecida!!!\n")
				self.conexao

		#Iniciando a Criptografia
		self.smtp_obj.starttls()

	def user_pass(self):
		#Recebendo o nome e o usuario
		self.nome = input("Username: ")
		self.passname = getpass("Password: ")

		return (self.nome, self.passname)

	def log_in(self):

		while True:

			try:
				#fazendo login com o método "login()"
				self.smtp_obj.login(self.nome, self.passname)
				print("Logado")
				break
			except smtplib.SMTPAuthenticationError:
				print("Nome de Usuário e/ou Senha não está incorreto(a)\n")
				self.user_pass()

	def enviar_email(self):
		#TO ->> Para quem?
		self.TO = input("TO: ")
		#Titulo do Email
		self.TITLE_SUB = input("Title of the Subject: ")
		#Texto Principal
		self.SUBJECT = input("Subject: ")

		try:
			#Enviando email com sendmail
			self.smtp_obj.sendmail(self.nome, self.TO, "Subject: "+self.TITLE_SUB+"\n"+self.SUBJECT)

		except smtplib.SMTPSenderRefused:
			print("""Você precisa habilitar a opção "PERMITIR APLICATIVOS MENOS SEGUROS" em sua conta!!!
Habilite pelo seguinte link: https://myaccount.google.com/lesssecureapps?pli=1""")

	def Sair(self):
		#Deslogar
		self.smtp_obj.quit()

		

#test = SendEmail()
