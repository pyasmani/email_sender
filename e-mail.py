import smtplib
import time
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
from os import walk
s = None
def connect():
	s = smtplib.SMTP('mail.host.com:25')
	s.starttls()
	s.login('username','password')
	return s

def disconnect():
	try:
		s.quit()
	except Exception as e:
		raise e

def email_you(me,you,file):
    msg = MIMEMultipart()
    msg['Subject'] = '{}. {} de 3 emails'.format(file.split('.')[0],file.split('.')[2])
    print 'Sending mail ' + msg['Subject']
    msg['From'] = me
    msg['To'] = you
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("./files/%s"%(file), "rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' %(file))
    msg.attach(part)
    s.sendmail(me, [you], msg.as_string())
    
def ls(ruta = './files'):
	return sorted(next(walk(ruta))[2])

if __name__ == '__main__':
	me = "emailorigin@mail.com"
	you = "emaildest@mail.com"
	s = connect()
	for x in ls():
		time.sleep(1)
		email_you(me,you,str(x))
	disconnect()

