import smtplib

to = 'dima.mindibekov@mail.ru' 
gmail_user = 'dmitriymindibekov@gmail.com'
gmail_pwd = 'DimonAs007qwerty123'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo() #команда приветствия
smtpserver.starttls() #шифрование по протоколу TLS
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
print (header)
msg = header + '\n Hello brroo \n\n'
smtpserver.sendmail(gmail_user, to, msg)
print ('done!')
smtpserver.close()
