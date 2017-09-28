#sending gmail using python
#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
#starting smtplib
s.starttls()
#logging in  using gmail 
s.login("karankumarbabu@gmail.com","karanajith")
#typing message
message="hi"
#sending mail
s.sendmail("karankumarbabu@gmail.com","karankumarbabu@gmail.com",message)
s.quit()
