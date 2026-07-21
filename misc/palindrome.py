text = input()
text_len = len(text)

left = 0
right = text_len-1

while(left<right):
    if text[left] != text[right]:
        break
    else:
        left+=1
        right-=1
