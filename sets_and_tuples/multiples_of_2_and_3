# find the multiples of 2 and 3 and print the sorted list of multiples of 2 but not 3 and the sorted list of uncommon multiples.
n=int(input())
multiples_of_2=[]
multiples_of_3=[]
for i in range(1,n+1):
    num=2*i 
    multiples_of_2.append(num)
for i in range(1,n+1):
    num=3*i 
    multiples_of_3.append(num)
set_a=set(multiples_of_2)
set_b=set(multiples_of_3)
mul_of_2_but_not_3= set_a.difference(set_b)
uncommon_multiples=set_a.symmetric_difference(set_b)
print(sorted(list(mul_of_2_but_not_3)))
print(sorted(list(uncommon_multiples)))
