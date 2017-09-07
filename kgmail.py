#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("karankumarbabu@gmail.com","karanajith")
message="hi"
s.sendmail("karankumarbabu@gmail.com","karankumarbabu@gmail.com",message)
s.quit()
