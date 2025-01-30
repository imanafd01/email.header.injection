# Email Header Injection: Setup and Demonstration Guide

This guide explains how to set up a local environment to test an **Email Header Injection** attack using **MailHog**. The goal is to understand the vulnerabilities related to email headers and experiment with sending a spoofed email via a local SMTP server.

## Why Use MailHog?
MailHog is a lightweight, local SMTP testing tool that captures emails without actually sending them to real inboxes. It allows for safe email testing by simulating an email server, making it an ideal solution for evaluating vulnerabilities such as email header injection.

**Warning**: This project is for educational purposes only and must be used in a controlled environment. Any unauthorized attempt to attack third-party systems is illegal.

---

## Prerequisites

1. **Python 3 installed**: Verify with the command:
   ```bash
   python3 --version
   ```
   If Python is not installed, download it from [python.org](https://www.python.org/).

2. **Docker installed**: MailHog runs via Docker. Check if Docker is installed:
   ```bash
   docker --version
   ```
   Download it from [docker.com](https://www.docker.com/) if necessary.

3. **Basic command line knowledge**: You should be comfortable running commands in a terminal.

---

## Installation and Configuration

### Step 1: Clone this Git repository
Run the following command to retrieve the project:

```bash
git clone https://github.com/your-username/email-header-injection.git
cd email-header-injection
```

### Step 2: Install and Start MailHog
MailHog is a simple tool that captures emails sent through a local SMTP server. We will use it to view emails without them actually reaching an inbox.

#### Option 1: Run MailHog with Docker (Recommended)
Start MailHog:

```bash
docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog
```
- `-d`: Runs MailHog in the background.
- `-p 1025:1025`: Opens the SMTP port on 1025.
- `-p 8025:8025`: Allows access to the MailHog web interface.

Verify that MailHog is running by accessing [http://localhost:8025](http://localhost:8025) in your browser.

#### Option 2: Run MailHog as a Binary (Without Docker)
Download MailHog:

```bash
wget https://github.com/mailhog/MailHog/releases/download/v1.0.1/MailHog_linux_amd64
```

Make it executable:

```bash
chmod +x mailhog__amd64
```

Run MailHog:

```bash
./mailhog_amd64
```

You can then access [http://localhost:8025](http://localhost:8025) to view captured emails.

### Step 3: Run the Email Injection Script
The Python script `email_injection.py` sends a spoofed email by manipulating headers. Execute it with:

```bash
python3 email_injection.py
```

#### Script Explanation:
- **Real sender**: `evil.sender@mail.com`
- **Simulated recipient**: `my.mail@mail.com`
- **Injected headers**:
  - `From: your.mom@outlook.com` (Hides the sender's real identity)
  - `X-Mailer: Microsoft Outlook` (Makes it appear as if sent from Outlook)
  - `Reply-To: evil.sender@example.com` (Redirects replies to the attacker)
  - `X-Injected-Header: Safe mail` (Adds a custom header)

The email content is a fraudulent message requesting a bank transfer.

---

## Viewing Emails in MailHog
After executing the script, open [http://localhost:8025](http://localhost:8025) to view the captured email.

You should see:
- The email with the falsified sender address `your.mom@outlook.com`.
- The injected headers in MailHog's **Raw** tab.
- The body of the message containing the fraudulent request.

---

## Risks and Impact of Email Header Injection
Email header injection is a serious vulnerability exploited for:
- **Identity spoofing**: The attacker falsifies the sender address to impersonate a trusted individual.
- **Phishing**: The email may contain a malicious link prompting the victim to enter personal information.
- **Financial fraud**: The attacker may send fake payment or bank transfer requests.
- **Reputation damage**: A company’s name can be used to send spam or fraudulent emails.

---

## Security Measures to Prevent This Attack
### Strict validation of user inputs:
- Disallow line breaks (`\r`, `\n`) in **From**, **To**, and **Subject** fields.
- Reject inputs containing `<script>` or other malicious HTML tags.

### Use secure SMTP servers:
- Enable **SPF**, **DKIM**, and **DMARC** on your domain to prevent identity spoofing.

### Do not trust incoming email headers:
- Verify the sender’s authenticity by inspecting the **Received** header.

---

## Conclusion
This project demonstrates how email header injection can be exploited to deceive recipients. The goal is to raise awareness of the risks and protective measures.

**Key takeaways**:
- Simple header modifications can mislead recipients.
- MailHog enables safe testing of these attacks.
- Good cybersecurity hygiene is essential to prevent email fraud.

**Disclaimer**
This project is for educational purposes only. Exploiting vulnerabilities outside an authorized environment is illegal.

---

## References
- [MailHog Documentation](https://github.com/mailhog/MailHog)
- [SMTP Injection Vulnerability Guide](https://owasp.org/www-community/vulnerabilities/SMTP_Injection)
- [DKIM, SPF & DMARC Explained](https://dmarc.org/)
