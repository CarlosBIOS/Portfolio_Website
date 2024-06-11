import smtplib
import ssl
import os


def send_emails(message):
    host: str = 'smtp.gmail.com'
    port: int = 465

    username: str = 'portfoliowebsitepython@gmail.com'
    # password: str = 'xxxx ...' # Não é a maneira mais correta e segura de guardar uma senha, mas no futuro vamos ver
    # qual é a maneira mais segura de guardá-la, ou seja, com environment variables!!!

    # Como guardar uma pass de maneira segura:
    # Vou ter que criar uma environment variável no meu local host, portanto, como sou Windows tenho que seguir estes
    # passos(Se quiser ver os outros OS, ver o vídeo 225 apartir de 4:50):
    # 1: Procurar por: Editar as variáveis de ambiente no sistema
    # 2: Carregar no último botão chamado: variáveis de ambiente
    # 3: Carregar no primeiro botão de novo, na seção: variáveis de utilizador para cmmon
    # 4: Preencher na 1 com o nome que dei na variável, ou seja, PASSWORD_PORTFOLIO_WEBSITE, e na outra, a pass!!
    password: str | None = os.getenv('PASSWORD_PORTFOLIO_WEBSITE')
    receiver: str = username  # Por exemplo

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
