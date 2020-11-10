import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from Include.GlobalValues import *

def register_mail(receiver):
    register_msg = MIMEText(register_html1 + str(price) + register_html2, _subtype='html', _charset='utf-8')
    register_msg['Subject'] = register_subject
    register_msg['From'] = sender
    register_msg['To']=receiver
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, register_msg.as_string())
    smtp.quit()