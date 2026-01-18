# find the index of a number in a nested list and print the index.
num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
n=int(input())
for tuple_a in num_list:
    if n in tuple_a:
        indexx = num_list.index(tuple_a)
        n_index = tuple_a.index(n)
print("{} {}".format(indexx,n_index))