from program_features.message import MotivationalMessage
from program_features.my_email import Email
from program_features.receiver_data import get_receiver_name_email
from program_features.current_weekday import get_current_weekday


def main(email, password, smtp, receiver_names, receiver_emails, message):
    email_details = {
        "sender_email": email,
        "sender_password": password,
        "sender_smtp": smtp,
        "receiver_names": receiver_names,
        "receiver_emails": receiver_emails,
        "message": message,
    }

    email = Email(email_details)

    today = get_current_weekday()

    delivery_day = "Monday"

    if today == delivery_day:
        email.deliver_email()
        
        
my_email = "example@email.com"  # Your email
password = "whatever_password"  # Your email password
smtp_host = "smtp_host"  # e.g. "smtp-mail.outlook.com" or "smtp.gmail.com"

receiver_names, receiver_emails = get_receiver_name_email("path/to/receivers.csv")

QUOTES_PATH = "path/to/quotes.txt"
LETTER_TEMPLATE_PATH = "path/to/letter_templates"  

message = MotivationalMessage(QUOTES_PATH, LETTER_TEMPLATE_PATH)

if __name__ == "__main__":
    main()    