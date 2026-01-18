# find the missing numbers in a list and print the sorted list.
def convert_to_int(num_list):
    new_list=[]
    for i in num_list:
        num=int(i)
        new_list.append(num)
    return new_list

list_a=input().split()
list_a=convert_to_int(list_a)
set_a=set(list_a)
maximum=max(list_a)
set_b=set(range(1,maximum+1))
missing_element= set_b.difference(set_a)
print(sorted(list(missing_element)))