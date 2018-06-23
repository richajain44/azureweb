from email.mime.text import MIMEText
import smtplib
def send_email(email, height):
	from_email="richaweb44@gmail.com"
	from_password="timepass591988"
	to_email=email
	
	subject= "Height Data"
	message=" Your height is %s." % height
	print(message)
	msg =MIMEText(message,'html')
	msg['Subject']=subject
	msg['To']=to_email
	msg['From']=from_email
	gmail =smtplib.SMTP('smtp.gmail.com',587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(from_email,from_password)
	print(msg['To'],msg['From'])
	gmail.send_message(msg)