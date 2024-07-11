import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pyhtml2pdf import converter
import schedule
import time
import os
from robot import run as run_robot


def run_robot_tests(robot_test_file, log_html):
    # Run the Robot Framework tests
    run_robot(robot_test_file, log=log_html)


def convert_html_to_pdf(html_file, output_pdf):
    converter.convert(f'file:///{html_file}', output_pdf)
    print(f"PDF created successfully at {output_pdf}")


def send_email(subject, body, attachment_path):
    sender = "sahithisahu98@gmail.com"
    smtp_password = "hrnx eosp ljnx hauq"
    recipient = "sahithiaddagarla98@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    with open(attachment_path, "rb") as attachment:
        # Instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
        # To change the payload into encoded form
        p.set_payload(attachment.read())
        # Encode into base64
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
        # Attach the instance 'p' to instance 'msg'
        msg.attach(p)

    # Create SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, smtp_password)
        text = msg.as_string()
        server.sendmail(sender, recipient, text)
    print("Email sent successfully")


def run_scheduled_task():
    robot_test_file = 'C:/Users/A. Sahithi/PycharmProjects/CardinalHealth/Testing/login.robot'
    log_html = 'C:/Users/A. Sahithi/PycharmProjects/CardinalHealth/Testing/log.html'
    output_pdf = 'C:/Users/A. Sahithi/PycharmProjects/CardinalHealth/Testing/output.pdf'

    run_robot_tests(robot_test_file, log_html)

    convert_html_to_pdf(log_html, output_pdf)

    subject = "Test Email"
    body = "Please find the attached report."
    send_email(subject, body, output_pdf)


if __name__ == "__main__":
    # Schedule the task
    schedule.every().day.at("14:07").do(run_scheduled_task)

    while True:
        schedule.run_pending()
        time.sleep(1)
