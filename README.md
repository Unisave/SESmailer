
# Mailer Script for automated CRM with mail generated using Jinja blueprint using AWS SES API for delivery 
## Abridged Algorithm
### Mail dependency libraries Import
##### 1. AWS Credentials and Network Configuration settings implementation for SES AWS Account. 
###### EMAIL_PORT variations temporarily set AWS = 25,465,587
### Email creation
##### 2. Message header content and data integration / compilation
##### 3. Message body content and data integration from JINJA or any other templating service as HTML file
###### html = open('<FILENAME/PATH to Jinja generated mail file.html>').read()
###### mime_text = MIMEText(html, '<Email content data format type>')
### Mailing core operations and functions performing using sendmail()
##### Optional TLS security embed for email 
##### SES Mail Service logon and 
### ===Session close===
