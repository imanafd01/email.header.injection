# Email Header Injection: Docker Setup and Exploitation Guide

This guide explains how to set up a Dockerized environment for testing Email Header Injection. We will use MailHog, an open-source email testing tool that captures outgoing emails sent from a local development environment, allowing us to test email functionality without sending real emails and to demonstrate, ethically, how email headers can be manipulated. This project is for **educational purposes only** and should be used in a controlled environment.

## Prerequisites

1. **Python Installed**: Ensure Python is installed on your system.
   - Check with:
     ```bash
     python --version
     ```
   - Download from [python.org](https://www.python.org/downloads/) if necessary.

2. **MailHog installed**: Verify with the command:
   ```bash
   mailhog --version
   ```
   If MailHog is not installed, download it from [MailHog Releases](https://github.com/mailhog/MailHog/releases).

3. **Docker Installed**: Ensure Docker is installed on your system.
   - Check Docker version:
     ```bash
     docker --version
     ```
   - Install from [docker.com](https://www.docker.com/) if necessary.

4. **Basic Command Line Knowledge**: Ability to navigate and run commands in the terminal.

---

## **Setting Up the Environment**

Start by downloading all the files in one , navigate to the folder's directory and run cmd.

### **Step 1: Create a Docker Network**

We first create a Docker network to allow communication between containers:

```bash
docker network create email_network
```

If a Docker network already exists, delete it and create a new one:

```bash
docker network rm email_network
docker network create email_network
```



### **Step 2: Run MailHog in Docker**

MailHog will act as a fake SMTP server to capture and display emails.

```bash
docker run -d --network=email_network --name mailhog -p 8025:8025 -p 1025:1025 mailhog/mailhog
```

- `-d` → Runs MailHog in the background.
- `--network=email_network` → Ensures it can communicate with the email injection script.
- `--name mailhog` → Names the container "mailhog".
- `-p 8025:8025` → Exposes the MailHog web interface.
- `-p 1025:1025` → Exposes the SMTP server on port 1025.

Verify that MailHog is running:

```bash
docker ps
```

Then, open MailHog's web UI:

[MailHog Web Interface](http://localhost:8025)

### **Step 3: Build and Run the Email Injection Script in Docker**

Before running the email injection script, you need to **build the Docker image** from the files provided in this repository.

#### **1 Build the Docker Image**
Navigate to the directory containing the cloned repository and run:

```bash
docker build -t email-header-injection .
```

This will create a Docker image named **email-header-injection**.

#### **2️ Run the Email Injection Script in Docker**
Once the image is built, execute the following command to run the container and connect it to MailHog:

```bash
docker run --rm --network=email_network -e SMTP_HOST="mailhog" -e SMTP_PORT="1025" email-header-injection
```

- `--rm` → Automatically removes the container after execution.
- `--network=email_network` → Connects to the MailHog container.
- `-e SMTP_HOST="mailhog"` → Uses MailHog as the SMTP server.
- `-e SMTP_PORT="1025"` → Uses port 1025 for SMTP communication.

After running this command, check MailHog to see the captured email:  
 **[http://localhost:8025](http://localhost:8025)**


---

## **Understanding Email Header Injection**

### **What is Email Header Injection?**

Email header injection is a security vulnerability where an attacker manipulates email headers to:

- Spoof sender information (make emails appear from trusted sources).
- Redirect replies to a different email address.
- Inject custom headers for malicious purposes.

### **How Does the Attack Work?**

1. A vulnerable email-sending script allows user inputs to be injected into email headers.
2. An attacker manipulates headers to modify the `From`, `Reply-To`, or `CC` fields.
3. The victim receives a spoofed email that appears legitimate.

### **Example of Injected Headers**

The following script manipulates headers before sending an email:

```python
headers = {
    "From": "your.mom@outlook.com",
    "To": "victim@mail.com",
    "Subject": "Emergency",
    "X-Mailer": "Microsoft Outlook",
    "Reply-To": "attacker@example.com",
    "X-Injected-Header": "Safe mail"
}
```

This can make the email look like it was sent by `your.mom@outlook.com`, even though it was actually sent from another address.

---

## **Mitigation Strategies**

To prevent Email Header Injection, developers should:

- **Sanitize User Inputs**: Disallow newline characters (`\r`, `\n`) in email headers.
- **Use Secure SMTP Authentication**: Ensure email servers enforce proper authentication mechanisms.
- **Enable SPF, DKIM, and DMARC**: These email security standards help prevent spoofing.
- **Avoid Direct User Input in Headers**: Use predefined templates for emails instead of dynamic user inputs.

---

## **Key Takeaways**

This guide demonstrated how to:

- Set up a Docker environment for testing email header injection.
- Run MailHog to safely capture spoofed emails.
- Execute an email injection attack in a controlled setting.
- Understand the risks and mitigation strategies.

**Disclaimer**: This guide is for educational and ethical security testing purposes only. Do not use this information for illegal activities.
