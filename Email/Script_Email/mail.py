# -*- coding:utf-8 -*-

try:
    import init
except Exception as er:
    print(er) #TEMPORÁRIO
    exit()


from init import smtp_obj
from smtplib import SMTPAuthenticationError, SMTPSenderRefused
from time import sleep
from getpass import getpass
from os.path import basename

#Class for generating application/* MIME documents.
from email.mime.application import MIMEApplication

#Base class for MIME multipart/* type messages.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pdb import set_trace

#COMMASPACE é usada para unir uma lista de muitos endereços de email
#em uma string para inserção na mensagem
from email.utils import COMMASPACE, formatdate

class DESMail():
    def __init__(self):
        self.smtp_obj = smtp_obj


    def User_Pass(self, name=None, password=None):
        '''
        Método irá receber uma entrada do usuário
        informando o nome(name) e a senha(password)
        '''
        #set_trace() #DEBUG
        while True:
            #Recebendo o nome e a senha
            if (name and password) is not None:
                self.name = name
                self.password = password
                break

            else:
                self.name = input("Email: ")
                self.password = getpass("Password: ")
                break

        return (self.name, self.password)



    def Log_In(self):
        '''
        Method used to log in using the name and password
        entered by the user.
        '''
        while True:
            try:
                #fazendo login com a função "login()"
                self.smtp_obj.login(self.name, self.password)
                self.Logged = True
                print("Logged") #TEMPORÁRIO
                break
            except SMTPAuthenticationError:
                print("User and/or password incorrect\n") #TEMPORÁRIO



    def Log_Out(self):
        '''
        Leave a section.
        '''
        if self.Logged:
            self.smtp_obj.quit()
            self.Logged=False
            print("Logout")
        else:
            print("Usuário Não está logado") #TEMPORÁRIO



    def Email_Details(self, send_to,title, text, files=None):
        '''
        Método para enviar o email
        '''
        self.email_send = False
        self.send_to = send_to
        self.files = files

        #Instanciando um objeto para juntar várias partes de um email:
        #De quem?, para quem?, data, conteúdo
        self.msg = MIMEMultipart()
        self.msg['From'] = self.name
        #Juntando a sting(caso ela esteja separada por espaço)
        self.msg['To'] = COMMASPACE.join(self.send_to)
        #Hora '-'
        self.msg['Date'] = formatdate(localtime=True)
        self.msg['Subject'] = title
        #Texto do email
        #Inserir From, To, Date, Subject ao email.
        self.msg.attach(MIMEText(text))

        for file in self.files:
            with open(file, "rb") as fl:
                self.part = MIMEApplication(
                    fl.read(),
                    Name=basename(file)
                        )

                #Apresentação do corpo da resposta como um arquivo para download.
                self.part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
                #Inserindo um anexo.
                self.msg.attach(self.part)




    def Send_Mail(self):
        try:
            #Enviando email com sendmail
            self.smtp_obj.sendmail(self.name, self.send_to,self.msg.as_string())
            self.email_send = True
            print("EMAIL ENVIADO")

        except SMTPSenderRefused:
            return  """Você precisa habilitar a opção "PERMITIR APLICATIVOS MENOS SEGUROS" em sua conta!!!
Habilite pelo seguinte link: https://myaccount.google.com/lesssecureapps?pli=1"""




    def Info(self):
        '''
        Some Information about the last email sent:
        From, to, files sent, day and hour

        '''
        if len(self.files) > 1:
            self.files = self.files.join(",")
        if not self.email_send:
            print("Você não enviou nenhum email. ")

        print("""+----------------------------+
| Informações sobre o Email. |
+============================+
From: %s
To: %s
Files Sent: %s
Day: %s
Hour: %s""" %(self.name,self.send_to, self.files, self.msg["Date"][0:16], self.msg["Date"][17:25]))