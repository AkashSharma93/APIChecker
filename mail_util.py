from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import api_status
import os

# Email config data.
email_to = "present.akash@gmail.com"
email_from = "APIChecker@test.com"
email_subject = "API Checker - Status"

# SMTP settings.
smtp_host = "smtp.gmail.com"
smtp_port = 465
smtp_login = os.environ["smtp_login"]	# There is currently no validation added to check these two properties
smtp_password = os.environ["smtp_password"]

# Send mail using the status passed to this method.
def send_mail(status):
	receipients = email_to.split(",")
	mail_body = "API Status changed to: " + status.get_api_status()

	# Configure SMTP.
	smtp = smtplib.SMTP_SSL(host=smtp_host, port=smtp_port)
	smtp.ehlo()
	smtp.login(smtp_login, smtp_password)

	# Send mail to all receipients.
	for receipient in receipients:
		receipient = receipient.strip()
		message = MIMEMultipart()
		message["From"] = email_from
		message["To"] = receipient
		message["Subject"] = email_subject

		message.attach(MIMEText(mail_body, "plain"))
		smtp.sendmail(email_from, receipient, message.as_string())