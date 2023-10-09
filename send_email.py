
# 运行结束发送邮件

import time
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Mylog:
    def __init__(self, tag=None):
        time_info=str(time.strftime("%m_%d_%H", time.localtime()))
        if not os.path.exists('./runlogs/'):
            os.mkdir('./runlogs/')
        if tag:
            time_info += tag
        self.file_name='./runlogs/'+time_info+'.log'
        self.file=open(self.file_name, 'a')

    def __del__(self):
        self.file.close()

    def add_log(self,lg):
        #添加日志记录
        time_info = str(time.strftime("%Y-%m-%d %H:%M:%S -->  ", time.localtime()))
        self.file.write(time_info+lg)
        self.file.write('\r')
        self.file.flush()

    def send_mail(self):
        #运行结束后发送邮件
        self.file.close()
        from_addr = ''  # 邮件发送账号
        to_addrs = ''  # 接收邮件账号
        qqCode = ''  # 授权码（这个要填自己获取到的）
        smtp_server = 'smtp.qq.com'
        smtp_port = 465

        # 配置服务器
        stmp = smtplib.SMTP_SSL(smtp_server, smtp_port)
        stmp.login(from_addr, qqCode)

        with open(self.file_name,'r') as f:
            buffer=f.read()

        # 组装发送内容
        subject = 'AUTODL-运行结束'
        send_user = 'autodl'

        message = MIMEText(buffer, 'plain', 'utf-8')  # 发送的内容
        message['From'] = Header(f"{send_user} <{from_addr}>")  # 发件人
        message['To'] = Header("me", 'utf-8')  # 收件人
        message['Subject'] = Header(subject, 'utf-8')  # 邮件标题
        try:
            stmp.sendmail(from_addr, to_addrs, message.as_string())
            print('邮件发送成功')
        except Exception as e:
            print('邮件发送失败--' + str(e))
