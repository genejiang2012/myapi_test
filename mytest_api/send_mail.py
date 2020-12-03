import smtplib

from email.mime.text import MIMEText

# port: 25, send the mail with no encrypt
smtp_server = smtplib.SMTP_SSL(host="smtp.126.com", port=465)
smtp_server.login(user='youthjiang@126.com', password='VALUACWGKKZGVOCH')

content = "This is a message mail!"
subject = "helloworld"
from_user = "youthjiang@126.com"
to_user = "genejiang2012@outlook.com"

my_mail = MIMEText(content, _subtype="plain", _charset="utf-8")
my_mail["From"] = from_user
my_mail["To"] = to_user
my_mail["subject"] = subject

smtp_server.send_message(my_mail)
print("Done")