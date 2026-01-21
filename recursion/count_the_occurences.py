#count the occurences of the numbers in the list 
s=input().split()
L=[]

for i in s:
    if s.count(i)%2!=0:
        if i not in L:
            L.append(i)
for i in range(len(L)):
    L[i]=int(L[i])
print(sorted(L))