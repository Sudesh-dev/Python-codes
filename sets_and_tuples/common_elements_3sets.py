# find the common elements in three sets and print the sorted list.
def convert(num_list):
    new_list=[]
    for item in num_list:
        num=int(item)
        new_list.append(num)
    return new_list

list_a=input().split()
list_a=convert(list_a)
set_a=set(list_a)
list_b=input().split()
list_b=convert(list_b)
set_b=set(list_b)
list_c=input().split()
list_c=convert(list_c)
set_c=set(list_c)

set_ab=set_a.intersection(set_b)
set_abc= set_ab.intersection(set_c)

common_list=list(set_abc)
common_list.sort()
print(common_list)
