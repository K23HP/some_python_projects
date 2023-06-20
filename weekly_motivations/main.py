from program_functions.current_weekday import get_current_weekday
from program_functions.email import Email
from program_functions.email_delivery import deliver_email
from program_functions.random_quote import generate_random_quotes

random_quote = generate_random_quotes()

email = Email("khantpaing123@outlook.com", "dr.zin28@gmail.com", random_quote)

today = get_current_weekday()

if today == "Tuesday":
    deliver_email(email, password="Nanjing2019")