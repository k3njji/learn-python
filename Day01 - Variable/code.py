#printing code
print("hello world")

#printing many lines
print("hello\nworld")
print("hello" + "world!")

#input and printing
data = input("what is your name? ")
print(f"hello {data}")
print("hello " + input("what is your name? ") + "!")

#exercise
glass1 = "milk"
glass2 = "juice"

temp = glass1
glass1 = glass2
glass2 = temp
print(f"{glass1} ans {glass2}")