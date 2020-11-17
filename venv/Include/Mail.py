import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from Include.GlobalValues import *


def register_mail(receiver):
    register_msg = MIMEText(register_html1 + str(price.get()) + register_html2, _subtype='html', _charset='utf-8')
    register_msg['Subject'] = register_subject
    register_msg['From'] = sender
    register_msg['To'] = receiver
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, register_msg.as_string())
    smtp.quit()


def update_mail(receiver):
    update_msg = MIMEText(update_html, _subtype='html', _charset='utf-8')
    update_msg['Subject'] = update_subject
    update_msg['From'] = sender
    update_msg['To'] = receiver
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, update_msg.as_string())
    smtp.quit()
