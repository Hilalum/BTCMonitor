import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

smtpserver = 'smtp.88.com'
username = 'BTCMonitor@88.com'
password='PDhdeFNCnVzuzHWt'
sender='BTCMonitor@88.com'
receiver=['dcyap0@icloud.com']

subject = '注册成功'


#构造html
#发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>
html = """
    <p style="text-align: center;font-weight:bold;font-size:35px;"><br><br>
    Hi<br>  
       恭喜你<br>  
       成功注册BTCMonitor账户！<br> 
       <br><br><br><br>
    </p> 
"""
msg = MIMEText(html,_subtype='html', _charset='utf-8')
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = ";".join(receiver)

def register_mail():
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()