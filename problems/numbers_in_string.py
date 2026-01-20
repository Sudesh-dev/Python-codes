# print the sum and average of the numbers in the string.
sentence = input().split()
numbers_list=[]
for i in sentence:
    numbers=""
    for j in i:
        if j.isdigit():
            numbers+=j
    if numbers!="":
        numbers_list.append(numbers)
digit_list = []

for dig in numbers_list:
    for j in dig:
        num= int(j)
        digit_list.append(num)

print(sum(digit_list))
avg = sum(digit_list)/len(digit_list)
avg = round(avg,2)
print(avg)