import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Retrieve SMTP settings from environment variables
SMTP_HOST = os.getenv("SMTP_HOST", "mailhog")  # Must match the MailHog container name
SMTP_PORT = int(os.getenv("SMTP_PORT", 1025))  # Use port 1025

# Define sender and receiver
sender_email = "evil.sender@mail.com"  # The real sender's email
receiver_email = "my.mail@mail.com"  # The victim's email

# Injected Headers
headers = {
    "From": "your.mom@outlook.com",
    "To": receiver_email,
    "Subject": "Emergency",
    "X-Mailer": "Microsoft Outlook",  # Identifies the email client
    "Reply-To": "evil.sender@example.com",
    "X-Injected-Header": "Safe mail"  # Custom header injection
}

# Create the email
msg = MIMEMultipart()
msg["From"] = headers["From"]
msg["To"] = headers["To"]
msg["Subject"] = headers["Subject"]
msg["Reply-To"] = headers["Reply-To"]
msg["X-Mailer"] = headers["X-Mailer"]

body = "This is an emergency, I'll call you later, send me 10000 dollars to this account XXXXXXXXXXXX. Mom"
msg.attach(MIMEText(body, "plain"))

# Send email through MailHog SMTP server
try:
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:  # Connect to MailHog
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Fake email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
