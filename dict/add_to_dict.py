# add a new item to the dictionary and print the dictionary.
students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
item = input().split()
students_dict[item[0]]=item[1]
print(students_dict)