# remove a number from all the tuples in a nested list and print the list of tuples.
num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]
n=int(input())
new_list=[]
for tuple_a in num_list:
    list_a=list(tuple_a)
    if n in list_a:
        list_a.remove(n)
    tuple_a=tuple(list_a)
    new_list.append(tuple_a)
    
print(new_list)