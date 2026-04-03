# list comprehension
# new_list = [new_item for item in list]

# add 1 for numbers in new_list
numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]

name = 'angle'
letter_list = [n for n in name]
print(letter_list)

doubled = [n*n for n in range(1, 5)]
print(doubled)

names = ['Merab', 'Alex', 'Oliveira', 'Topuria', 'Volkanovski', 'Diego', 'Conor', 'Khabob',]

names_under_four = [n for n in names if len(n) <= 5]
print(names_under_four)

# dictionary comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = [new_key: new_value for (key, value) in dict.items()]
names = ['Merab', 'Alex', 'Oliveira', 'Topuria', 'Volkanovski', 'Diego', 'Conor', 'Khabob',]

import random

random_score = {student:random.randint(0, 100) for student in names}
print(random_score)

passed_score = {key:value for (key, value) in random_score.items() if value > 70}
print(passed_score)

for(key, value) in passed_score.items():
    print(key, value)

import pandas as pd

student_df = pd.DataFrame(list(random_score.items()), columns=["name", "score"])
print(student_df)

for index, row in student_df.iterrows():
    print(row["name"], row["score"])