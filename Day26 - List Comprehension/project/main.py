student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

import pandas
data = pandas.read_csv("Day26 - List Comprehension/project/nato_phonetic_alphabet.csv")
print(data.head())

name_dict = {}

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

for (index, row) in data.iterrows():
    print(row['letter'], row['code'])
    name_dict.update(((row['letter'], row['code']), ))

print(name_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

output = []

def phonetric():
    name = input("write a name and get the phonetic: ").upper()
    try:
        for n in name:
            output.append(name_dict[n])
    except KeyError:
        print('sorry only letter in the alphabet')
        phonetric()
    else:
        print(output)

phonetric()