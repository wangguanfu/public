import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from qacenter.settings import EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD


def send_password(receiver, password):
    if '@sina.com' in EMAIL_SEND_USERNAME:
        smtp_server = 'smtp.sina.com'
    elif '@163.com' in EMAIL_SEND_USERNAME:
        smtp_server = 'smtp.163.com'
    else:
        smtp_server = 'smtp.exmail.qq.com'

    subject = "质量中心新密码"
    smtpPort = '465'

    body = MIMEText("您的新密码：" + password + "，请查收，谢谢！", _subtype='html', _charset='gb2312')

    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['from'] = EMAIL_SEND_USERNAME
    msg['to'] = receiver
    msg.attach(body)

    try:
        smtp = smtplib.SMTP_SSL(smtp_server,smtpPort)
        smtp.connect(smtp_server)
        smtp.starttls()
        smtp.login(EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD)
        smtp.sendmail(EMAIL_SEND_USERNAME, receiver.split(','), msg.as_string())
        smtp.quit()
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

if __name__ == '__main__':
    send_password('##@qq.com, example@163.com', '123456789')
