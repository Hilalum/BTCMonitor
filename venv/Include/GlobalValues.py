from email.mime.text import MIMEText
import queue

price = queue.Queue()
# 邮件配置
smtpserver = 'smtp.88.com'
username = 'BTCMonitor@88.com'
password = 'PDhdeFNCnVzuzHWt'
sender = 'BTCMonitor@88.com'

register_html1 = """<p style="text-align: center;font-weight:bold;font-size:35px;"><br><br>Hi<br>恭喜你<br>成功注册BTCMonitor账户！<br><br>当前BTC价格为$"""
register_html2 = """<br><br>春风得意马蹄疾，一日看尽长安花<br>祝你好运<br><br><br><br></p> """
register_subject = '注册成功'

update_html = """<p style="text-align: center;font-weight:bold;font-size:35px;"><br><br><br><br>BTCMonitor账户信息发生变更，请确保此次变动是您自己操作！<br><br><br><br><br><br><br><br><br></p>"""
update_subject = '账户变更'

# 接口配置
BTCUrl = "https://sochain.com/api/v2/get_price/BTC/USD"
GVZUrl = "https://sochain.com/api/v2/get_price/BTC/USD"
VIXUrl = "https://sochain.com/api/v2/get_price/BTC/USD"
sleep_times = 5
