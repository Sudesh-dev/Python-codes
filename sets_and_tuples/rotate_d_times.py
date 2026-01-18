# rotate a list d times to the right and print the rotated list.
def convert(num_list):
    new_list=[]
    for i in num_list:
        num=int(i)
        new_list.append(num)
    return new_list

list_a= input().split(",")
d=int(input())
list_a = convert(list_a)
list_len=len(list_a)
d = d % list_len

part_1 = list_a[:d]
part_2 = list_a[d:]
part_2.extend(part_1)
print(part_2)
