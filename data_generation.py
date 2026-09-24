import random


def generate_email():
    random_number = random.randint(100, 999)
    return f"arsen_vartanov_54_{random_number}@yandex.ru"


def generate_password():
    random_number = random.randint(100000, 999999)
    return f"Password{random_number}"