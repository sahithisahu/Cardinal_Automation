import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'sahithisahu98@gmail.com'
EMAIL_PASSWORD = '********************'

contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'This is a Python Test for Sending a Email automated'
msg['From'] = EMAIL_ADDRESS
# msg['To'] = 'YourAddress@gmail.com'
msg['To'] = EMAIL_ADDRESS

msg.set_content('The attachment need to be filed or attached.')

files = ['C:\\Users\\balur\\OneDrive\\Desktop\\testFile.pdf']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
smtp.send_message(msg)
