import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from Include.GlobalValues import *

def register_mail(receiver):
    register_msg['To']=receiver
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, register_msg.as_string())
    smtp.quit()