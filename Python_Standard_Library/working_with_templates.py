from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

# Normally use templates in another file to make up the body of an email
# Use HTML to build the template

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Bryan Miller"
message["to"] = "testuser@bryanmil.com"
message["subject"] = "This is a test"
# body = template.substitute({ "name": "Chris XD"}) # Passing dictionary
body = template.substitute(name="Chrissy") # Passing key word arguments insteaad here
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("bryan.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser@bryanmil.com", "todayskyisblue111")
    smtp.send_message(message)
    print("Sent...")