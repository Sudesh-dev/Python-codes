# find the maximum and minimum values in the first and second index of a nested list and print the pairs.
n=int(input())
def convert(listt):
    new_list=[]
    for i in listt:
        num=int(i)
        new_list.append(num)
    return new_list
    
zero_index_list=[]
one_index_list=[]
for i in range(n):
    values=input().split()
    values=convert(values)
    
    zero_index_list.append(values[0])
    one_index_list.append(values[1])

zero_max=max(zero_index_list)
zero_min=min(zero_index_list)

one_max=max(one_index_list)
one_min=min(one_index_list)

pair_a= (zero_max, zero_min)
print(pair_a)

pair_b= (one_max, one_min)
print(pair_b)