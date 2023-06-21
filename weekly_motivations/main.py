from program_components.message import MotivationalMessage
from program_components.my_email import Email
from program_components.receiver_data import get_receiver_name_email
from program_functions.current_weekday import get_current_weekday

my_email = "Your email"
password = "Your email password"
smtp_host = "Your Email SMTP"  # e.g. "smtp-mail.outlook.com" or "smtp.gmail.com"

receiver_names, receiver_emails = get_receiver_name_email("path/to/receivers.csv")

QUOTES_PATH = "path/to/quotes.txt"
LETTER_TEMPLATE_PATH = "path/to/letter_templates"  

message_generator = MotivationalMessage(QUOTES_PATH, LETTER_TEMPLATE_PATH)

# Create 
email_details = {
    "sender_email": my_email,
    "sender_password": password,
    "sender_smtp": smtp_host,
    "receiver_names": receiver_names,
    "receiver_emails": receiver_emails,
    "message_generator": message_generator,
}

email = Email(email_details)

today = get_current_weekday()

if today == "Monday":
    email.deliver_email()
