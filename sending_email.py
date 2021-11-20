import smtplib
import getpass   # For hidden passwords


smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()

email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your password: ")
smtp_object.login(email,password)

from_address = getpass.getpass("Enter your email: ")
to_address = getpass.getpass("Enter the email of the recipient: ")
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address,to_address,msg)

smtp_object.quit()

