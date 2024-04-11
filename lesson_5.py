from random import randint as generate_number, choice
import utils.calculator as calc
from utils.person import Person
from termcolor import cprint
import emoji
from decouple import config

print(generate_number(1, 10))
print(calc.addition(1, 6))

my_friend = Person('Bob', 30)
print(my_friend)

cprint("Hello, World!", "green", "on_yellow")
print(emoji.emojize('Python is :thumbs_up:'))

print(config('DATABASE_URL'))

commented = config('COMMENTED', default=0, cast=int)
print(commented * 2)
# Comment