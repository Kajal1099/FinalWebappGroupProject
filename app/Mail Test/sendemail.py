import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path


def absolute_path(filepath):
    relative = Path(filepath)
    return relative.absolute()


def sendemail(to, strHash):
    sender_email = "kajal1099@gmail.com"
    receiver_email = to
    password = 'Dwlyist345!'

    message = MIMEMultipart("alternative")
    message["Subject"] = "Verify Student email for access to class resources"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    Hi Student,
    You have Sign Up for the Student database.
    Please click on link to verify email."""

    html = """\
    <html>
      <body>
        <p>Hi,<br>
           You have Sign Up for the Student database.<br><br>
           <a href="http://0.0.0.0:5000/validateLogin/""""" + strHash + """">Click Here</a> 
           to validate your email address.
        </p>
      </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

   
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
        server.quit()
