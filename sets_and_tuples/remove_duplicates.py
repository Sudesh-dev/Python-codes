input_list=input().split()
new_list= []
for i in input_list:
    num=int(i)
    new_list.append(num)
new_set=set(new_list)
new_list=list(new_set)
new_list.sort()
print(new_list)
