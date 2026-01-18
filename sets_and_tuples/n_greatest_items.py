# find the n greatest items in a list and print them in sorted order.
list_a = [5, 20, 3, 7, 6, 8]
list_a.sort()
k = int(input())
list_len = len(list_a)
res = list_a[list_len - k:]
for i in range(k):
    res[i] = str(res[i])
print(" ".join(res))
