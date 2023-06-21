import pandas as pd


def get_receiver_name_email(data_dir):
    data = pd.read_csv(data_dir)
    receiver_names = data["name"].to_list()
    receiver_emails = data["email"].to_list()

    return (receiver_names, receiver_emails)
    