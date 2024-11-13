from datetime import datetime


def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime("%m-%d-%Y")
    try:
        valid_date = datetime.strptime(date_str, "%m-%d-%Y")
        return valid_date.strftime("%m-%d-%Y")


def get_amount(prompt):
    pass


def get_category(prompt):
    pass


def get_description(prompt):
    pass
