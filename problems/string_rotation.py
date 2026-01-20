# check if the second string is a rotation of the first string and
# print the index of the first letter of the second string in the first string.
str1=input()
str2=input()

if  len(str1)==len(str2):
    first_letter = str1[0]
    if first_letter in str2 and len(str1)==len(str2):
        print(str2.index(first_letter))
    else:
        print("No Match")
else:
    print("No Match")