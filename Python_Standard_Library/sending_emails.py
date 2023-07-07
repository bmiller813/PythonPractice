# Make sure to handle exceptions with a try bloc
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "Bryan Miller"
message["to"] = "testuser@bryanmil.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body", "plain"))
message.attach(MIMEImage(Path("bryan.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser@bryanmil.com", "todayskyisblue111")
    smtp.send_message(message)
    print("Sent...")
