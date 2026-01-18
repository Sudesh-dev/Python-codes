# find the unique pairs of numbers in a list that add up to a given sum and print the sorted pairs.
def convert(num_list):
    new_list=[]
    for i in num_list:
        num=int(i)
        new_list.append(num)
    return new_list
def get_unique_pairs(list_a , sum_pairs):
    stop_index= len(list_a)-1
    unique_pairs_set = set()
    for cur_index in range(stop_index):
        num_1=list_a[cur_index]
        num_2=sum_pairs- num_1
        remaining_list = list_a[cur_index+1:]
        if num_2 in remaining_list:
            pair= (num_1,num_2)
            sorted_pair= tuple(sorted(pair))
            unique_pairs_set.add(sorted_pair)
    return unique_pairs_set
    

list_a=input().split(",")
list_a=convert(list_a)
sum_pairs=int(input())
unique_pair= get_unique_pairs(list_a,sum_pairs)
unique_pair= list(unique_pair)
unique_pair.sort()
for pain in unique_pair:
    print(pain)