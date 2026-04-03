# water_level = 50
# if water_level > 80:
#     print("drain water")
# else:
#     print("continue")

# if else and nested if
print("welcome to roller coaster")
height = int(input("whats your height? "))

if(height >= 120):
    print("you can take this ride")
    age = int(input("input your age: "))
    if(age < 12):
        print("you have to pay 5$")
    elif(age > 18):
        print("you have to pay $12")
    elif(age > 45 and age <55):
        print("free rride")
    else:
        print("you have to pay $7")
    
    want_photo = input("do you want to also have the photo? (type yes or no)")
    if(want_photo == 'yes' or want_photo == 'y'):
        print("additional $3")        
else:
    print("you cant")

# modulo
print(10%3)

# odd or even
number = int(input("input a number to check whether this is odd or even: "))
if(number%2 == 1):
    print("this is odd")
else:
    print("this is even")