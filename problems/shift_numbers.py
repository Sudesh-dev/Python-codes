# shift the numbers to the end of the string and print the result.
user_input = input()

letter = ""
numbers = ""

for i in user_input:
    if i.isalpha():
        letter+=i
    else:
        numbers+=i 
result = letter+numbers
print(result)