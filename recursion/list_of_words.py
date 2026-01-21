#remove the words that start with 'a' from the list and print the list.
s=input().split()
L=[]
for i in s:
    if not i.startswith('a'):
        L.append(i)
print(L)