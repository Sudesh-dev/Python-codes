# check if the set is a subset, superset or disjoint set.
num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
def convert(num_list):
    new_list=[]
    for i in num_list:
        num=int(i)
        new_list.append(num)
    return new_list

list_a= input().split()
list_a=convert(list_a)
set_a=set(list_a)
if num_set.issuperset(set_a):
    print("Superset")
elif num_set.issubset(set_a):
    print("Subset")
elif num_set.isdisjoint(set_a):
    print("Disjoint Set")