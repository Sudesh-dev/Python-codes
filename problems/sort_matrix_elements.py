# sort the elements of a matrix and print the sorted matrix.
def to_int(listt):
    new_list=[]
    for i in listt:
        num=int(i)
        new_list.append(num)
    return new_list

m,n = input().split()
m= int(m)
n= int(n)
matrix =[]
for i in range(m):
    row = input().split()
    row = to_int(row)
    matrix.append(row)
    
element_list=[]

for i in matrix:
    for j in i:
        element_list.append(j)
element_list.sort()
k=0
for i in range(m):
    for j in range(n):
        matrix[i][j]=element_list[k]
        k+=1

for row in matrix:
    print(*row)
