import smtplib
import ssl


def send_emails(message):
    host: str = 'smtp.gmail.com'
    port: int = 465

    username: str = 'portfoliowebsitepython@gmail.com'
    password: str = 'whbb qmgg ixbu hbgg'  # Não é a maneira mais correta e segura de guardar uma senha, mas no futuro
    # vamos ver qual é a maneira mais segura de guardá-la!!!
    receiver: str = username  # Por exemplo

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
