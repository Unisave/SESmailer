#Import mail dependency libraries
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# AWS Configuration settings for SES AWS Account
with open('mailerConfig.json') as json_data_file:
	maildata = json.load(json_data_file)
	EMAIL_HOST = maildata["email"]["host"]
	EMAIL_HOST_USER = maildata["email"]["user"]
	EMAIL_HOST_PASSWORD = maildata["email"]["passwd"]
	EMAIL_PORT = maildata["email"]["port"]


# EMAIL_PORT variations for AWS = 25,465,587

# Address book 
with open('mailerContacts.json') as json_data_file:
	me = mailCon["emailcontact"]["me"]
	you = mailCon["emailcontact"]["you"]

# Message header content and data integration / compilation
with open('mailerContents.json') as json_data_file:
	msg = MIMEMultipart('alternative')
	msg['Subject'] = mailcontent["email"]["subject"]
	msg['From'] = me
	msg['To'] = you
	contentName = mailcontent["email"]["contentFile"]
	html = open(contentName).read()
# Message body content and data integration from JINJA or any other templating service as HTML file
# html = open('<FILENAME/PATH to Jinja generated mail file.html>').read()



mime_text = MIMEText(html, 'html')
# mime_text = MIMEText(html, '<Email content data format type>')
msg.attach(mime_text)

# Mailing core operations and functions performing using sendmail()
s = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
# Optional TLS security embed for email 
s.starttls()
# SES Mail Service logon and 
s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
s.sendmail(me, you, msg.as_string())
# Session close
s.quit()

