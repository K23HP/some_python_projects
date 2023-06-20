from smtplib import SMTP

def deliver_email(email: object, password: str):
    # Create a connection to my_email
    with SMTP("smtp-mail.outlook.com") as connection:
        # Create Transport Layer Security (TLS) for connection
        connection.starttls()

        # Email login
        connection.login(user=email.sender, password=password)

        # Send Email
        connection.sendmail(
            from_addr=email.sender, 
            to_addrs=email.reciever, 
            msg=f"From: {email.sender}\nTo: {email.reciever}" + \
                f"\nSubject: Tuesday Motivation!\n\n{email.message}"  
        )
    print(f'✅ Email sent to "{email.reciever}".')    