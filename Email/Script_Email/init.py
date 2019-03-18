from smtplib import SMTP

smtp_obj = ''

def connect():
	global smtp_obj
	while True:
		try:
			smtp_obj = SMTP("smtp.gmail.com",587)
			#Iniciando a Criptografia
			smtp_obj.starttls()
			#self.hot_obj = smtplib.SMTP("smtp-mail.outlook.com", 587)
			break
			#Se não estiver conectado a internet, o python irá levantar um erro(socket.gaierror) ->> IGNORAR
		except Exception as er:
			return er
	print("Tudo OK") #TEMPORÁRIO
	# return True

connect()