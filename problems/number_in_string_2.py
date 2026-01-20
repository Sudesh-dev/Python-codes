# print the sum and average of the numbers in the string.
sentence = input()
num_list=[]
numbers = ""
for ch in sentence:
    if ch.isdigit():
        numbers+= ch
    else:
        if numbers!="":
            num_list.append(int(numbers))
            numbers=""
if numbers!="":
    num_list.append(int(numbers))

total = sum(num_list)
print(total)
avg = total/ len(num_list)
print(round(avg,2))