from email.mime.text import MIMEText
price = 0
smtpserver = 'smtp.88.com'
username = 'BTCMonitor@88.com'
password='PDhdeFNCnVzuzHWt'
sender='BTCMonitor@88.com'
#构造html
#发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>
register_html = """
    <p style="text-align: center;font-weight:bold;font-size:35px;"><br><br>
    Hi<br>  
       恭喜你<br>  
       成功注册BTCMonitor账户！<br> 
       <br><br><br><br>
    </p> 
"""
register_subject = '注册成功'
register_msg = MIMEText(register_html,_subtype='html', _charset='utf-8')
register_msg['Subject'] = register_subject
register_msg['From'] = sender