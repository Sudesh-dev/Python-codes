# add an item to a set and print the sorted list.
set_a = {"pencil"}

word = input()
set_a.add(word)

list_a = list(set_a)
list_a.sort()
print(list_a)