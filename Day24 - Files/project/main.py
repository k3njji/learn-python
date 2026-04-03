#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Day24 - Files/project/Input/Letters/starting_letter.txt", "r") as file:
    template = file.read()

with open("Day24 - Files/project/Input/Names/invited_names.txt", "r") as file:
    names = file.read().splitlines()

for name in names:
    personalized_letter = template.replace("[name]", name)

    with open(f"Day24 - Files/project/Output/ReadyToSend/letter_for_{name}.txt", "w") as new_file:
        new_file.write(personalized_letter)