import random
#making our own module
import my_module

#random integer (inclusive)
randomInteger = random.randint(1, 100)
print(randomInteger)

print(my_module.pi)

randomFloat = random.random()*10
print(randomFloat)

randomFloatAnother = random.uniform(0, 10)
print(randomFloatAnother)

#lists
#unlike in other programming language, [] in python is a lists not an array. Lists is dynamic and we can do many things with it

#head or tails
words = ['Head', 'Tail']
randomIndex = random.randint(0, 1)
print(words[randomIndex])

states_of_america = ['delaware', 'pennsylvania', 'alaska', 'arizona']
print(states_of_america[0])
print(states_of_america[-1])

states_of_america.append("canada")
print(states_of_america[-1])

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits.count('apple')
# 2
# fruits.count('tangerine')
# 0
# fruits.index('banana')
# 3
# fruits.index('banana', 4)  # Find next banana starting at position 4
# 6
# fruits.reverse()
# fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
# fruits.append('grape')
# fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# fruits.sort()
# fruits
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
# fruits.pop()
# 'pear'
