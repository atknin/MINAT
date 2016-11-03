import smtplib

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.starttls()
smtpserver.login('dmitriymindibekov@gmail.com','DimonAs007qwerty123')
smtpserver.sendmail("dima.mindibekov@mail.ru","Xakac19rus@mail.ru", "Myb roro")

