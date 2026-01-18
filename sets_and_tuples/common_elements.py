# find the common elements in two lists and print them in sorted order.
def convert_string_to_int(list):
    new_list=[]
    for item in list:
        num=int(item)
        new_list.append(num)
    return new_list


list_a =input().split(",")
list_b = input().split(",")
list_a= convert_string_to_int(list_a)
list_b= convert_string_to_int(list_b)

set_a=set(list_a)
set_b=set(list_b)

common_elements= set_a.intersection(set_b)
common_elements_list=list(common_elements)
common_elements_list.sort()
print(common_elements_list)
