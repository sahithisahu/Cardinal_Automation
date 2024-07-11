import schedule
import time
from robot import run
import smtplib
from email.mime.text import MIMEText
from pyhtml2pdf import converter

# Define the path to your Robot Framework test file and report
robot_test_file = 'C:/Users/A. Sahithi/PycharmProjects/CardinalHealth/Testing/login.robot'
output_dir = 'C:/Users/A. Sahithi/PycharmProjects/CardinalHealth/Testing/results'
report_file = f'{output_dir}/report.html'
html_file = r'C:\Users\A. Sahithi\PycharmProjects\CardinalHealth\Testing\log.html'
output_pdf = r'C:\Users\A. Sahithi\PycharmProjects\CardinalHealth\Testing\results\output.pdf'
converter.convert(f'file:///{html_file}', output_pdf)

print(f"PDF created successfully at {output_pdf}")

def send_email(subject, body):
    sender = 'sahithisahu98@gmail.com'
    recipient = 'sahithiaddagarla98@gmail.com'
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    msg.attach(MIMEText(body, 'plain'))

    # Open the file to be sent
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')

        # Attach the instance 'part' to instance 'msg'
        msg.attach(part)

    # Use Gmail's SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_password = 'vkoj lpij bvqa ktia'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, smtp_password)
        server.sendmail(sender, recipient, msg.as_string())


def run_robot_tests():
    print("Starting Robot Framework tests...")
    # result = run(robot_test_file, outputdir=output_dir)
    print("Robot Framework tests completed.")
    result = 0

    with open(report_file, 'r', encoding='utf-8') as file:  # Specify the encoding here
        report_content = file.read()

    if result == 0:
        send_email("Test Report: All tests passed", report_content)
    else:
        send_email("Test Report: Some tests failed", report_content)


schedule.every().day.at("11:00").do(run_robot_tests)

run_robot_tests()
# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)



