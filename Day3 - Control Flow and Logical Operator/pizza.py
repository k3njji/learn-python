print("welcome to python pizza deliveries!")
size = input("what size of pizza do you want? s, m, or l: ")
pepperoni = input("do you want peperonu on your pizza? y or n: ")
cheese = input("do you want extra cheese? y or n: ")

bill = int()

if(size == 's'):
    bill = 15
    if(pepperoni == 'y'):
        bill += 2
elif(size == 'm'):
    bill = 20
else:
    bill = 25

if(pepperoni == 'y' and (size == 'm' or size == 'l')):
    bill += 3

if(cheese == 'y'):
    bill += 1

print("your total bill is ", bill)