import smtplib
from email.mime.text import MIMEText

def send_reminder(subject, body, to_email, from_email, password):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, password)
        server.send_message(msg)

if __name__ == "__main__":
    # Replace with your details before running
    send_reminder("Reminder", "This is your reminder!", "to@example.com", "from@example.com", "yourpassword")