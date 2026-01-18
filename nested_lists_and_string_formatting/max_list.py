# find the maximum number in each nested list and print the list of maximum numbers.
def convert(listt):
    new_list=[]
    for i in listt:
        num=int(i)
        new_list.append(num)
    return new_list

n=int(input())
max_list=[] 
for i in range(n):
    value_list=input().split()
    value_list=convert(value_list)
    max_num= max(value_list)
    max_list.append(max_num)
print(max_list)
    