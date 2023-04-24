import random
import string
from datetime import date

month_names = {
    1: "JAN",
    2: "FEB",
    3: "MAR",
    4: "APR",
    5: "MAY",
    6: "JUN",
    7: "JUL",
    8: "AUG",
    9: "SEP",
    10: "OCT",
    11: "NOV",
    12: "DEC"
}

def generate_password(first_name):
    current_year = date.today().year
    return f'{first_name}@{current_year}'


counter = 0

def generate_id():
    global counter
    counter += 1
    return f"{counter:05d}"

def generate_username():
    current_year = str(date.today().year)[2:4]
    current_month = month_names.get(date.today().month)
    count = generate_id()
    return f'{current_year}{current_month}{count}'

def auto_username_password_generator(data):
    names = data['full_name'].split(' ')
    first_name = names[0]
    if len(names) == 1:
        last_name = "XXX"
    elif len(names) == 2:
        last_name = names[1]
    else:
        last_name = f'{names[1]} {names[2]}'
    data["first_name"] = first_name
    data["last_name"] = last_name
    data["username"] = generate_username()
    data["password"] = generate_password(first_name)
    del data["full_name"]
    
    return data