# print the longest common prefix of two strings and print "No overlapping" if there is no overlapping.
string_a = input().strip()
string_b = input().strip()
res=""
for i in range(len(string_a),0,-1):
    if string_a[-i:] == string_b[:i]:
        print(string_a[-i:])
        break
else:
    print("No overlapping")