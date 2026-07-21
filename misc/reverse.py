x = 1234

rev_val = 0
count = 0
while x>0:
    y = x%10
    rev_val = (rev_val*10)+y 
    x//=10
    count +=1
print(rev_val)

print(count)
