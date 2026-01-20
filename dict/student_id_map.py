# map the student id to the student name and print the dictionary.
key_ip = input().split(",")
value_ip = input().split(",")
def convert_to_dict(key_ip,value_ip):    
    students_dict={}
    for i in range(len(key_ip)):
        keys= key_ip[i]
        values= value_ip[i]
        students_dict[keys]=values
    return students_dict

students_dict = convert_to_dict(key_ip,value_ip)

student_items = students_dict.items()
students_details = sorted(student_items)

for i in students_details:
    print(*i)