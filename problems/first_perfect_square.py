# print the first perfect square between two numbers and print "No Perfect Square" if there is no perfect square.
a=int(input())
b=int(input())
count = 0
for i in range(a,b+1):
    square_root =  i**0.5 
    is_perfect_square = square_root== int(square_root)
    if is_perfect_square:
        print(i)
        break

else:
    print("No Perfect Square")