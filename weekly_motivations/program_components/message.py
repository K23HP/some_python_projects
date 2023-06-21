import os
import random


class MotivationalMessage:
    def __init__(self, quote_dir, letter_template_dir) -> None:
        self.quote_dir = quote_dir
        self.letter_template_dir = letter_template_dir
    
    
    def choose_random_letter_template(self, directory: str) -> str:
        filenames = os.listdir(directory)
        chosen_file = random.choice(filenames)
        return f"{chosen_file}"
    
    
    def create_a_list_of_lines(self, file_dir: str) -> list:
        with open(file_dir, 'r') as f:
            return f.readlines()
        
        
    def generate_random_string(self, file_dir: str):
        lines = self.create_a_list_of_lines(file_dir)
        return random.choice(lines)
    
    
    def replace_specific_expression(self, file_dir, expression_to_replace, replacement):
        with open(file_dir, 'r') as f:
            data = f.read()
            data = data.replace(f"{expression_to_replace}", replacement)

        return data

    def generate_motivational_message(self, name) -> str:
        quote = self.generate_random_string(self.quote_dir)
        template_name = self.choose_random_letter_template(self.letter_template_dir)
        message_template_dir = f"{self.letter_template_dir}/{template_name}"
        message_lines = self.create_a_list_of_lines(message_template_dir)
        
        message = ""
        
        for line in message_lines:
            if "[MESSAGE]" in line:
                new_line = line.replace("[MESSAGE]", quote)
                message += new_line
                
            elif "[NAME]" in line:
                new_line = line.replace("[NAME]", name)
                message += new_line  
            else:
                message += line
                
        return message