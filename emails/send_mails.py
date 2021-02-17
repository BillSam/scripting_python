import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Testing'
email['to'] = 'getelvest@gmail.com'
email['subject'] = 'Yu won '

# email.set_content('I am a python master')

email.set_content(html.substitute(name='Tin Tin'), 'html')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('@gmail.com', 'helloztmmyoldfriend1')
    smtp.send_message(email)
    print("All good")
