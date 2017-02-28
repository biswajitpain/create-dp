import smtplib
import sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 

def SendMail(to_name, to_addr, attachment_file_path):

	fromaddr = "<from your email id>"
	toaddr = to_addr
 
	msg = MIMEMultipart()
 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Your filtered DP"
 
	body = "Hi" + to_name + "Thanks for " 
 
	msg.attach(MIMEText(body, 'plain'))
 
	filename = attachment_file_path.strip()
	attachment = open(filename, "rb")
 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
	msg.attach(part)
 
	server = smtplib.SMTP('smtp-relay.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "your password")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

if __name__ == '__main__':
	to_name = sys.argv[1]
	to_addr = sys.argv[2]
	attachment_file_path = sys.argv[3]
	SendMail(to_name, to_addr, attachment_file_path)
