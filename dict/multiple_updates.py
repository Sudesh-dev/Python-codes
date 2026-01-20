# update the dictionary with multiple items and print the dictionary.
students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
n=int(input())
for i in range(n):
    item= input().split()
    key,value= item[0],item[1]
    students_dict[key]=value
print(students_dict)
    