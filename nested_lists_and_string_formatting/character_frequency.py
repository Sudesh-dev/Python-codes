# find the frequency of each character in a string and print the character and its frequency.
def print_char_count(string):
    string=string.lower()
    unique_chars= set(string)
    unique_chars.discard(" ")
    
    for char in sorted(unique_chars):
        print("{}: {}".format(char,string.count(char)))

string = input()
print_char_count(string)