# convert a nested list of strings into a list of tuples of integers.
def convert_nested_list_to_list_of_tuples(nested_list):
    # Complete this function
    tuples_list_a=[]
    for i in nested_list:
        value_tuple = tuple(i)
        tuples_list_a.append(value_tuple)
    return tuples_list_a


def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


n = int(input())
num_list = []

for i in range(n):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)


tuples_list = convert_nested_list_to_list_of_tuples(num_list)
print(tuples_list)
