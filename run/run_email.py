import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime

class SendEmail:
    global sender
    global password
    global email_host
    sender = '2504301482@qq.com'  # 发送人邮箱
    password = 'rjtnqimboqiqdijf'  # 发送人邮箱授权码
    email_host = 'smtp.qq.com'

    def send_email(self,filepath,user_list,sub,content):
        user = '<'+sender+'>'

        # 创建一个带附件的实例
        msg = MIMEMultipart()
        msg['Subject'] = Header(sub,'utf-8')
        msg['From'] = user
        msg['To'] =';'.join(user_list)

        # 创建正文
        msg.attach(MIMEText(content, 'plain', 'utf-8'))

        # 构造附件
        filename = filepath
        time = datetime.date.today()
        att = MIMEText(open(filename,'rb').read(),'html','utf-8')
        att['Content-Type'] = 'application/octet-stream'
        # Content-Disposition:以什么方式打开
        att["Content-Disposition"]= 'attachment; filename="DGJAPItestresult.html"'
        msg.attach(att)

        # 邮箱设置时勾选了SSL加密连接，进行防垃圾邮件，SSL协议端口号要使用465
        smtp = smtplib.SMTP_SSL(email_host, 465)
        smtp.helo(email_host)
        # 向服务器标识用户身份
        smtp.helo(email_host)
        # 向服务器返回确认结果
        smtp.ehlo(email_host)
        # 登录邮箱的账号和授权密码
        smtp.login(sender, password)

        print("开始发送邮件")
        smtp.sendmail(sender,user_list,msg.as_string())
        print('邮件发送成功')
        smtp.close()

    def send_main(self):
        user_list = ['yuanxiangting@diyibox.com','guoyue@diyibox.com']
        sub = "递管家接口自动化测试报告"
        content = '接口自动化测试结果：见附件'
        filepath ="C:\\Users\\18838\\Desktop\\python脚本\\pythonProject3\\report\\expressin_report.html"
        self.send_email(filepath,user_list,sub,content)
if __name__ == '__main__':
    se = SendEmail()
    se.send_main()
