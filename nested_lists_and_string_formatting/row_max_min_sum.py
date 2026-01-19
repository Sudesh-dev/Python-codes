# Write a Python program that reads a matrix from the user and prints the maximum, minimum, and sum of the elements in each row.
def print_max_min_sum_for_row_wise(num_list):
    max_list=[]
    min_list=[]
    sum_list=[]
    for row in num_list:
        max_list.append(max(row))
        min_list.append(min(row))
        sum_list.append(sum(row))
    print(max_list)
    print(min_list)
    print(sum_list)
    
def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

print_max_min_sum_for_row_wise(num_list)
