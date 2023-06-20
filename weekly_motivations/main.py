from program_functions.current_weekday import get_current_weekday
from program_functions.email import Email
from program_functions.email_delivery import deliver_email
from program_functions.random_quote import generate_random_quotes

quote = generate_random_quotes()

my_email = "example@email.com"
password = "Your_email_password"
smtp_host = "Your email smtp host"  # e.g. "smtp-mail.outlook.com"

receiver_email = "reciever@email.com"

email = Email(my_email, password, smtp_host, receiver_email, quote)

today = get_current_weekday()

if today == "Monday":
    deliver_email(email)