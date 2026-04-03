import random
import string

print("welcome to password generator")
length = int(input("how many letters do you want? "))
symbol = int(input("how many symbol do you want? "))
numbers = int(input("how many numbers do you want? "))

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*",
    "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", "\\", "|",
    ";", ":", "'", "\"", ",", ".",
    "<", ">", "/", "?"
]

length = length - symbol - numbers

password = []

for i in range(length):
    password.append(random.choice(list(string.ascii_letters)))

for i in range(symbol):
    password.append(symbols[random.randint(0, len(symbols)-1)])

for i in range(numbers):
    password.append(str(random.randint(0, 9)))

real_password = []

random.shuffle(password)

for i in password:
    real_password+=i


print("your password is ", real_password)