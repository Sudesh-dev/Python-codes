def diagonal_star(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j or j+i==n+1:
                print("* ",end="")
            else:
                print("  ",end="")
        print()



def print_binary(n):
    for i in range(n):
        for j in range(i+1):
            if (i+j)%2==0:
                print(1,end="")
            else:
                print(0,end ="")
        print()

def binary_pattern_rev(n):
    for i in range(n):
        print(" "*(n-i-1),end="")
        for j in range(i+1):
            if (i+j)%2==0:
                print(1,end="")
            else:
                print(0,end="")
        print()


# print_binary(5)
binary_pattern_rev(5)
# diagonal_star(5)
