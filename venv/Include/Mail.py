import smtplib
import base64
from email.mime.text import MIMEText
from Include.GlobalValues import *


def register_mail(receiver):
    send(register_html1 + str(price.get()) + register_html2, receiver)


def update_mail(receiver):
    send(update_html, receiver)


def send(email_body, receiver):
    msg = MIMEText(email_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = update_subject
    msg['From'] = sender
    msg['To'] = receiver
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, base64.decodebytes(password).decode())
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()