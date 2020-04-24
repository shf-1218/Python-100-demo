# encoding: utf-8
"""
@version: 1.0
@author: 
@file: SendMail
@time: 2020-04-02 17:41
"""

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = '15701356807@163.com'
    receivers = ['1034232100@qq.com', '1246074958@qq.com', '15701356807@163.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = '15701356807@163.com'
    # message['To'] = '1034232100@qq.com'
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP("smtp.163.com", 25)  # 实例化smtp服务器
    smtper.login('15701356807@163.com', 'IPGNPECBAHCVPVML')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()
