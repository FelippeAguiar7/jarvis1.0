import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import login as lg 
import ListaDeEmails as ls
from email.mime.base import MIMEBase
from email import encoders

def enviar_email(cotacaoDolar, cotacaoEuro):

    corpo_email = """
    <p>Olá!</p>
    <p>Eu sou o Jarvis, e estou aqui para fornecer algumas informações financeiras.</p>
    <p>Trago aqui as cotações de duas moedas:</p>
    <ul>
        <li><strong>Cotação do Dólar:</strong> R$ {}</li>
        <li><strong>Cotação do Euro:</strong> R$ {}</li>
    </ul>
    <p>Tenho um gráfico anexo com o histórico dessas moedas para sua análise.</p>
    <p>Atenciosamente,</p>
    <p>Jarvis</p>
    """.format(cotacaoDolar, cotacaoEuro)

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    email_login = lg.email
    senha_login = lg.senha

    for lista_email in ls.Lista:
        destinatario = lista_email
        assunto = 'Informações Financeiras - Jarvis (Amigo do Felippe)'
        corpo = corpo_email

        #mensagem = email.message.Message()
        mensagem = MIMEMultipart()
        mensagem['From'] = email_login
        mensagem['To'] = destinatario
        mensagem['Subject'] = assunto
        mensagem.attach(MIMEText(corpo, 'html'))
        
        attchment = open("C:\\Users\\felip\\Projetos\\ProjetoJarvis\\graficoDolarEuro.png",'rb')
        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attchment.read())
        encoders.encode_base64(att)
        att.add_header('Content-Disposition', f'attachment; filename=graficoDolarEuro.png')
        attchment.close()
        
        mensagem.attach(att)
        
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(email_login, senha_login)
            server.sendmail(mensagem['From'], [mensagem['To']], mensagem.as_string().encode('utf-8'))
            print(f'Email enviado para: {destinatario}')
            server.quit()
        except Exception as e:
            print(f'Erro ao enviar email para {destinatario}: {e}')
#teste
#enviar_email("3.89")