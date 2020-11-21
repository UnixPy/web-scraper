import smtplib


def send_gmail(sender, reciever, token, subject, body):
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(sender, token)

        message = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(sender, reciever, message)

