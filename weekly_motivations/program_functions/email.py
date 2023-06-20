class Email:
    def __init__(self, sender: str, password: str, smtp_host: str, reciever: str, message: str) -> None:
        self.sender = sender
        self.password = password
        self.smtp_host = smtp_host
        self.reciever = reciever
        self.message = message
        