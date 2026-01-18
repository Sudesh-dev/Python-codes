# find the common elements in n sets and print the sorted list.
def convert(num_list):
    new_list=[]
    for i in num_list:
        num=int(i)
        new_list.append(num)
    return new_list

def get_intersections_of_sets(num_set_list):
    result= num_set_list[0]
    for num_set in num_set_list:
        result= result.intersection(num_set)
    return result

n=int(input())
num_set_list=[]
for i in range(n):
    list_a = input().split()
    list_a = convert(list_a)
    set_a = set(list_a)
    num_set_list.append(set_a)

result_set = get_intersections_of_sets(num_set_list)
result_list=list(result_set)
result_list.sort()
print(result_list)