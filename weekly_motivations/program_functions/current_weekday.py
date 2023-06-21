import datetime


def get_current_weekday():
    current_date = datetime.datetime.now()
    
    return current_date.strftime("%A")