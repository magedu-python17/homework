import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 配置邮箱账户及收发人信息
sender = 'zabbix@juneyaokc.com'
receivers = ['mingqiang.ning@juneyaokc.com', 'mingqiang.ning@juneyaokc.com']
mail_host = 'smtp.exmail.qq.com'
mail_user = 'zabbix@juneyaokc.com'
mail_pass = 'Jykc123,abc'

# 构建MIMEMultipart对象，并在其中添加邮件内容信息
message = MIMEMultipart()
message.attach(MIMEText('邮件测试', 'plain', 'utf-8'))
message['From'] = 'zabbix@juneyaokc.com'
message['To'] = 'mingqiang.ning@juneyaokc.com,mingqiang.ning@juneyaokc.com'
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 构建附件内容
attr = MIMEText(open('c:/test.txt','r').read())
attr['Content-Type'] = 'application/octet-stream'
attr['Content-Disposition'] = 'attachment; filename = ' + 'test.txt'
message.attach(attr)

# 发送邮件
try:
  smtpObj = smtplib.SMTP()
  smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
  smtpObj.login(mail_user,mail_pass)
  smtpObj.sendmail(sender, receivers, message.as_string())
  print("邮件发送成功！")
except smtplib.SMTPException:
  print("邮件发送失败！")


