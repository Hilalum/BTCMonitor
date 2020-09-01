# BTCMonitor
此为一个比特币监控和定投策略的小服务，随着项目进度，此文档将进一步完善。

###注册接口:register(GET)
#####参数：username pwd email weekmoney
##### 返回：{"msg": "注册成功"}/{'msg': '缺失参数'}
##### 注册成功发送以下邮件:
![Image text](https://raw.githubusercontent.com/dcyap0/BTCMonitor/master/res/mail.png)