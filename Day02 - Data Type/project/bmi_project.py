height = float(input("Input your height (in meters): "))
weight = float(input("Input your weight (in kgs): "))

bmi = weight/(height*height)

print(f"your bmi is {round(bmi, 2)}")