# Use an official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default environment variables
ENV SMTP_HOST=mailhog
ENV SMTP_PORT=1025

# Run the Python script
CMD ["python", "email_injection.py"]
