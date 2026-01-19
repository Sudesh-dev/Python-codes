# Write a Python program that reads a matrix from the user and prints the maximum, minimum, and sum of the elements in each column.
def get_transpose_of_matrix(matrix, m, n):
    transpose_matrix=[]
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(matrix[j][i])
        transpose_matrix.append(row)
    return transpose_matrix


def print_max_min_sum_for_row_wise(num_list):
    col_max=[]
    col_min=[]
    col_sum=[]
    for row in num_list:
        col_max.append(max(row))
        col_min.append(min(row))
        col_sum.append(sum(row))
    print(col_max)
    print(col_min)
    print(col_sum)


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
transpose_matrix = get_transpose_of_matrix(num_list,m,n) 
print_max_min_sum_for_row_wise(transpose_matrix)