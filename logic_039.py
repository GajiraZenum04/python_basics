import datetime
import random

def to_uppercase(text):
    return text.upper()
def get_today_date():
    return datetime.datetime.today().strftime("%y-%m-%d")
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
def generate_random_number():
    return random.randint(1, 100)
def my_full_name():
    return "Hannah Gajira"
