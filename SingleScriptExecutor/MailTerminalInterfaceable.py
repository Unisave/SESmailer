#Import mail dependency libraries
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import argparse
parser = argparse.ArgumentParser(description='This program was developed by Sooraj Antony to perform terminal level integration of the Mail server')
parser.add_argument('-s','--subject', help='Subject name eg: "Re: Hello"',required=True)
parser.add_argument('-r','--recipient',help='Recipient Mail ID eg: "bleh@meh.com"', required=True)
parser.add_argument('-m','--mailfile',help='Mail Content file location eg: "/path/to/location/of/mail/body.html"', required=True)
args = parser.parse_args()
## show values ##
subject = args.subject
recipient = args.recipient
mailbody = args.mailfile


# AWS Configuration settings for SES AWS Account
with open('mailerConfig.json') as json_data_file:
	maildata = json.load(json_data_file)
	EMAIL_HOST = maildata["email"]["host"]
	EMAIL_HOST_USER = maildata["email"]["user"]
	EMAIL_HOST_PASSWORD = maildata["email"]["passwd"]
	EMAIL_PORT = maildata["email"]["port"]


# EMAIL_PORT variations for AWS = 25,465,587

# Address book 
with open('mailerContacts.json') as json_data_file1:
	mailCon = json.load(json_data_file1)
	me = mailCon["emailcontact"]["me"]
	you = recipient

# Message header content and data integration / compilation
with open('mailerContents.json') as json_data_file2:
	msg = MIMEMultipart('alternative')
	mailcontent = json.load(json_data_file2)
	msg['Subject'] = subject
	msg['From'] = me
	msg['To'] = you
	contentName = mailbody
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

