# access the value of a nested list at a given index and print the list of values.

list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]

def convert(listt):
    new_list=[]
    for i in listt:
        num=int(i)
        new_list.append(num)
    return new_list

n=int(input())
result_list=[]

for i in range(n):
    index_list=input().split()
    index_list=convert(index_list)
    
    tuple_index=index_list[0]
    value_index=index_list[1]
    
    value=list_a[tuple_index][value_index]
    
    result_list.append(value)
print(result_list)
    
    
    