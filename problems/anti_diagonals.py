# print the anti-diagonals of a matrix.
def convert_to_int(listt):
    new_list=[]
    for i in listt:
        num = int(i)
        new_list.append(num)
    return new_list

m,n =input().split()
m=int(m)
n=int(n)
matrix=[]
for i in range(m):
    row = input().split()
    row = convert_to_int(row)
    matrix.append(row)

for sum in range (m+n-1):
    for i in range(m):
        for j in range(n):
            if i+j==sum:
                print(matrix[i][j],end=" ")
    print()
    
        