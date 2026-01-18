# convert a list of strings into a nested list of integers.
def convert(num_list):
    new_list=[]
    for i in num_list:
        num = int(i)
        new_list.append(num)
    return new_list

n=int(input())
nested_list=[]
for i in range(n):
    listt=input().split()
    listt=convert(listt)
    nested_list.append(listt)
print(nested_list)