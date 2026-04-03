weight = 85
height = 1.85

bmi = weight / (height ** 2)

if(bmi < 18.5):
    print("you are underweight")
elif(bmi > 25):
    print("you are overweight")
else:
    print("you are normal")