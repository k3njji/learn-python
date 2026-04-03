import math

#using len
print(f'Inside this word "Hello World!" contains {len("Hello World!")} numbers of characters')

#data types
#int
numbers = 1
print(f"{numbers} is an {type(numbers)}")

#float
decimal = 3.14
print(f"this is a float {decimal} where {type(decimal)}")

#boolean
truth = True
print(truth)

#string
word = "Word Example"
print(word)
print(f"This is the first character in the word {word[0]}")
print(f"This is the first character in the word {word[len(word)-1]}")

#concatating string
word += "? We can do this?"
print(word)

#type conversion
word = "1234"
print(f"this {word} is a {type(word)}")
numbers = int(word)
print(f"now this {numbers} is an {type(numbers)}")


print(f"your name is: {str(len(input('whats your name? ')))} characters")

#matemathical operators
print(f"addition {2 + 6}")
print(f"substraction {2 - 6}")
print(f"multiplication {2 * 6}")
print(f"division (float) {2 / 6}")
print(f"division (int) {int(2 / 6)}")
print(f"modulo {2 % 6}")

#rounding value
height = float(input("Input your height (in meters): "))
weight = float(input("Input your weight (in kgs): "))

bmi = weight/(height*height)

print(f"your bmi is {round(bmi, 2)}")
print(f"your bmi is {math.floor(bmi)}")
print(f"your bmi is {math.ceil(bmi)}")