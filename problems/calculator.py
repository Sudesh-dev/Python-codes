# calculate the result of a mathematical equation and print the result.
def calculate(num_1,operator,num_2):
    result = 0
    if operator=="+":
        result = num_1 + num_2
    elif operator=="-":
        result = num_1 - num_2
    elif operator=="*":
        result = num_1 * num_2
    elif operator=="/":
        result = num_1 / num_2
    elif operator=="%":
        result = num_1 % num_2
        
    
    return result

equation = input().split()
num_1 = int(equation[0])
operator = equation[1]
num_2 = int(equation[2])

res= calculate(num_1, operator, num_2)
print(res)