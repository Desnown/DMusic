import imapclient,  imaplib
from enviar_email import SendEmail 

class LerEmail():
	def __init__(self):
		#Usando a Criptografia SSL
		self.imap_obj = imapclient.IMAPClient("imap.gmail.com",ssl=True)

		while True:
			#Chamando a função user_pass do modulo enviar_email
			n,s = SendEmail().user_pass()

			try:
				self.imap_obj.login(n,s)
				#TENHO QUE ARRUMAR AQUI(RETURN)
				return "Connected"
				break
			except imapclient.exceptions.LoginError:
				print("Nome de Usuário ou Senha está incorreto(a)")

	def search_fold(self):
		#Procurando por pastas no gmail
		self.lista = list(self.imap_obj.list_folders())

		#Percorrendo estas pastas
		for i in self.lista:
			print(i)

	def select_fold(self,argv):
		try:

			#Selecionando uma Pasta
			#O metodo READONLY impede que faça modificação acidentalmente 
			print(self.imap_obj.select_folder(argv, readonly=True))

		except imapclient.exceptions.IMAPClientError:
			#caso nn encontre a Pasta
			print("Unknown Mailbox")

a = LerEmail()