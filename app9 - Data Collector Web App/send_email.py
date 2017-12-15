from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average_height, count):
    from_email = "neneriukas@gmail.com"
    from_password = "password"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <b>%s</b>. Average height of all is <b>%s</b> That is calculated out of <b>%s</b> people" % (
        height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_email(msg)
