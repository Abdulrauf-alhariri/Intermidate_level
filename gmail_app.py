from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class CommandLineAppliction:
    def __init__(self, user_gmail, user_password, to_gmail, message_text, from_who, Subject_message):

        self.user_gmail = user_gmail
        self.user_password = user_password
        self.to_gmail = to_gmail
        self.message_text = message_text
        self.from_who = from_who
        self.subject_message = Subject_message

    @classmethod
    def message_info(cls):
        try:
            from_who1 = input("Enter from who: ")
            user_gmail = input("Please enter your email: ")
            user_password = input("Please enter your password: ")
            print("\n")
        except:
            print("Unvaild gmail or password!")

        try:
            message_subject = input("Enter the subect or NONE: ")
            receiver = input("Enter the gmail of the receiver: ")
        except:
            print("Unvaild gmail")

        message_body = input("Enter the message: ")
        return cls(user_gmail, user_password, receiver, message_body, from_who1, message_subject)

    def send_email(self):

        # We are inherting the functions from the MIMEMultipart class
        message = MIMEMultipart()
        message["from"] = self.from_who
        message["to"] = self.to_gmail
        message["subject"] = self.subject_message

        # Here we are entering the body for the email
        message.attach(MIMEText(self.message_text))

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            # TO identify yourself to the smtp server
            smtp.ehlo()

            # To put all the commands in connection with the server
            smtp.starttls()

            # Here we are entering the gmail and password and then we are sending the message
            smtp.login(self.user_gmail, self.user_password)
            smtp.send_message(message)
            print("sent")


sned = CommandLineAppliction.message_info()
sned.send_email()
