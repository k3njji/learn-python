import random

student_scored = []

for i in range(100):
    student_scored.append(random.randint(0, 200))

total = 0
highest = 0

for i in student_scored:
    if( i > highest ):
        highest = i
    total += i

print(total)

print(highest)