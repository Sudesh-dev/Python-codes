# print the consecutive sum triangle of a list.
def convert_to_int(listt):
    new_list=[]
    for i in listt:
        num = int(i)
        new_list.append(num)
    return new_list

def get_consecutive_sum(elements):
    end_index=len(elements) - 1
    sum_list = []
    for i in range(end_index):
        summ = elements[i]+elements[i+1]
        sum_list.append(summ)
    return sum_list

def print_sum_triengle(cons_sum):
    while len(cons_sum)>1:
        consecutive_sum = get_consecutive_sum(cons_sum)
        print(consecutive_sum)
        cons_sum = consecutive_sum

elements = input().split(",")
elements = convert_to_int(elements)
print(elements)
print_sum_triengle(elements)