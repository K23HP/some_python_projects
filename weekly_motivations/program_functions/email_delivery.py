from smtplib import SMTP

def deliver_email(email: object):
    # Create a connection to my_email
    with SMTP(email.smtp_host) as connection:
        # Create Transport Layer Security (TLS) for connection
        connection.starttls()

        # Email login
        connection.login(user=email.sender, password=email.password)

        # Send Email
        connection.sendmail(
            from_addr=email.sender,  # Sender email
            to_addrs=email.reciever,  # Receiver email
            msg=f"From: {email.sender}\nTo: {email.reciever}" + \
                f"\nSubject: Tuesday Motivation!\n\n{email.message}"  
        )
    print(f'✅ Email sent to "{email.reciever}".')    