# count the number of words in a sentence and print the word and the number of times it appears in the sentence in sorted order.
sentence = input().split()
new_list=[]
for i in sentence:
    if i not in new_list:
        new_list.append(i)
new_list.sort()
for i in new_list:
    print("{}: {}".format(i,sentence.count(i)))