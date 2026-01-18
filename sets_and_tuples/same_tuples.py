# check if all the elements in the list are the same and print True if they are, otherwise print the sorted list.
def string_to_int(num_list):
    new_list=[]
    for item in num_list:
        num=int(item)
        new_list.append(num)
    return new_list

list_a=input().split()
int_list=string_to_int(list_a)

set_a= set(int_list)
list_a= list(set_a)
list_a.sort()
if len(set_a)==1:
    print(True)
else:
    print(list_a)