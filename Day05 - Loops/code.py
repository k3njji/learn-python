import random

#loops
fruits = ['apple', 'peach', 'pear']

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

print(fruits)

numbers = []

for i in range (0, 100):
    numbers.append(random.randint(0, 100))

for i in numbers:
    print(i)

for i in range (100, 0, -1):
    print(i)

while(True):
    print("true once")
    break

# fizzbuzz
for i in range (30):
    if(i%5 == 0 and i%3 == 0):
        print("FizzBuzz")
    elif(i%5 == 0):
        print("Buzz")
    elif(i%3 == 0):
        print("Fizz")