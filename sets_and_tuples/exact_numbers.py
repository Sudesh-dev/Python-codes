# remove elements other than numbers from a list and print the list.
def string_to_int(num_list):
    new_list=[]
    for item in num_list:
        if item.isdigit():
            num= int(item)
            new_list.append(num)
    return new_list


list_a=input().split(",")
list_a=string_to_int(list_a)
print(list_a)