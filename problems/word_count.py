# count the number of words in a sentence and print the word and the number of times it appears in the sentence.
seltence = input().split()
new_list=[]
for i in seltence:
    if i not in new_list:
        new_list.append(i)
        print("{}: {}".format(i,seltence.count(i)))