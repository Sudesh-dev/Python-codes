# delete an item from the dictionary and print the dictionary.
students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}

key = input()
del students_dict[key]
print(students_dict)