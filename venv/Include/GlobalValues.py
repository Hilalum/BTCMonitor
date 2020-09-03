from email.mime.text import MIMEText
price = 0
#邮件配置
smtpserver = 'smtp.88.com'
username = 'BTCMonitor@88.com'
password='PDhdeFNCnVzuzHWt'
sender='BTCMonitor@88.com'
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


#接口配置
url = "https://sochain.com/api/v2/get_price/BTC/USD"
sleep_times = 5