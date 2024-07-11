import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pyhtml2pdf import converter


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

    # Open the file to be sent
    with open(attachment_path, "rb") as attachment:
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")

        msg.attach(p)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, smtp_password)  # Login with mail_id and password
        text = msg.as_string()
        server.sendmail(sender, recipient, text)
    print("Email sent successfully")


def run_robot_tests():
    # Define paths
    html_file = r'C:\Users\A. Sahithi\PycharmProjects\CardinalHealth\Testing\results\report.html'
    output_pdf = r'C:\Users\A. Sahithi\PycharmProjects\CardinalHealth\Testing\results\output.pdf'

    # Convert the HTML file to PDF
    convert_html_to_pdf(html_file, output_pdf)

    # Send the PDF as an email attachment
    subject = "Test Email"
    body = "Please find the attached report."
    send_email(subject, body, output_pdf)


if __name__ == "__main__":
    import schedule
    import time

    # Schedule the task
    schedule.every().day.at("13:33").do(run_robot_tests)

    while True:
        schedule.run_pending()
        time.sleep(1)
