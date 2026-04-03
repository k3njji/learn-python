with open('Day24 - Files/myfile.txt', mode='w') as file:
    file.write("hehehe")
    file.close()

with open('Day24 - Files/myfile.txt', mode='a') as file:
    file.write("\naboy")
    file.close()

with open('Day24 - Files/myfile.txt') as file:
    content = file.read()
    print(content)
    file.close()

with open('Day24 - Files/myfile2.txt', mode='w') as file:
    file.write("hehehe2")
    file.close()