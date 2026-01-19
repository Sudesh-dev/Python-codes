# Write a Python program that reads a matrix from the user and prints the row and column containing the maximum element.
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

# Write your code here
max_list=[]

for row in num_list:
    max_list.append(max(row))

maximum = max(max_list)
row_index_containing_max= max_list.index(maximum)

max_row= num_list[row_index_containing_max]
print(max_row)

column_index_containing_max=max_row.index(maximum)
max_column=[]
for row in num_list:
    max_column.append(row[column_index_containing_max])
print(max_column)