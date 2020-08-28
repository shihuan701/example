import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host='smtp.qq.com'
mail_user='1335077456@qq.com'
mail_pass='dcfniwxtxrhfihag'
sender = '1335077456@qq.com'
receivers = ['sybil.shi@nf-3.com']
#创建一个实例
message = MIMEText(_text='大家好，\n\n\t\t\t 这是石一的日报', _subtype='plain', _charset='utf-8')
message['From'] = Header('1335077456@qq.com','utf-8')
message['To'] = Header('sybil.shi@nf-3.com','utf-8')
subject = 'sscm工作进度'
message['subject'] = Header(subject,'utf-8')

try:
    smtpObject = smtplib.SMTP()
    smtpObject.connect(mail_host,25)
    smtpObject.ehlo()
    smtpObject.starttls()
    smtpObject.login(mail_user,mail_pass)
    smtpObject.sendmail(sender,receivers,message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('邮件发送失败')


