from smtplib import SMTP


class Email:
    def __init__(self, email_details: dict) -> None:
        self.sender_email = email_details["sender_email"]
        self.sender_password = email_details["sender_password"]
        self.sender_smtp = email_details["sender_smtp"]
        self.receiver_names = email_details["receiver_names"]
        self.receiver_emails = email_details["receiver_emails"]  # List
        self.message = email_details["message"]
    
    
    def deliver_email(self):
        # Create a connection to my_email
        with SMTP(self.sender_smtp) as connection:
            # Create Transport Layer Security (TLS) for connection
            connection.starttls()

            # Email login
            connection.login(
                user=self.sender_email,
                password=self.sender_password
            )
            
            for i in range(len(self.receiver_emails)):
                # Send Email
                connection.sendmail(
                    from_addr=self.sender_email,  # Sender self
                    to_addrs=self.receiver_emails[i],  # Receiver self
                    msg=f"From: {self.sender_email}\nTo: {self.receiver_emails[i]}" + \
                        "\nSubject: Tuesday Motivation!" + \
                        f"\n\n{self.message.generate_motivational_message(self.receiver_names[i])}"
                )
                print(f'✅ Email sent to "{self.receiver_emails[i]}".')
        