# find the unique tuples in a nested list and print the list of unique tuples.
def convert(listt):
    new_list=[]
    for i in listt:
        num=int(i)
        new_list.append(num)
    return new_list

n=int(input())
unique_list=[]
for i in range(n):
    value_list=input().split()
    value_list=convert(value_list)
    set_a= set(value_list)
    if len(set_a)==len(value_list):
        unique_list.append(value_list)
print(unique_list)
        
    