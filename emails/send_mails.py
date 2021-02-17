import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Testing'
email['to'] = 'getelvest@gmail.com'
email['subject'] = 'Yu won '

email.set_content('I am a python master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('@gmail.com', 'helloztmmyoldfriend1')
    smtp.send_message(email)
    print("All good")
