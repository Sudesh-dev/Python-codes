# create a dictionary of squares of numbers from 1 to n and print the dictionary.
square_dict={}
n=int(input())

for i in range(1,n+1):
    square = i*i
    square_dict[i]=square
print(square_dict)