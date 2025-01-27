import smtplib

my_email = 'ddpythontest@yahoo.com'
password = 'ddpythontest1337'

connection = smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user=my_email, password=password)

connection.sendmail(from_addr=my_email, to_addrs="Dennis.klein87@gmail.com",msg="Du Knortz!")
connection.close()