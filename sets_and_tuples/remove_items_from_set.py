#  remove a list of numbers if present in the set.

num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
integers=input().split()
for i in integers:
    num = int(i)
    num_set.discard(num)
new_list= list(num_set)
new_list.sort()
print(new_list)