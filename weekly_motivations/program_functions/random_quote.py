import random

DATA_PATH = "./data/quotes.txt"

def create_quote_list(textfile_path: str) -> list:
    with open(textfile_path, 'r') as f:
        return f.readlines()
    
    
def generate_random_quotes():
    quotes = create_quote_list(DATA_PATH)
    
    return random.choice(quotes)