from celery import shared_task
from django.core.mail import send_mail
import datetime

@shared_task
def enviar_email_boas_vindas(nome, email):
    assunto = 'Bem-vindo ao nosso site!'
    mensagem = f'Olá {nome}, obrigado por se registrar no nosso site.'
    remetente = 'teste'
    destinatarios = [email]
    send_mail(assunto, mensagem, remetente, destinatarios)
    print(f'Email de boas-vindas enviado para {nome} pelo email: {email}')
    return f'Email de boas-vindas enviado para {nome} pelo emaul: {email}'

@shared_task
def heartbeat():
    now = datetime.datetime.now()
    print(f'Heartbeat: {now}')