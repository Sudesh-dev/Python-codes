# update the value of a key in the dictionary and print the dictionary.
students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}

# Write your code here
item = input().split()
key = item[0]
value= item[1]
students_dict[key]=value
print(students_dict)