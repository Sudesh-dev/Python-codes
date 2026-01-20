# rename a key in the dictionary and print the dictionary.
fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}

# Write your code here
key_1=input()
key_2=input()
fruit_items = list(fruits.items())
fruit_items_copy = fruit_items.copy()

for i in range(len(fruit_items_copy)):
    if fruit_items[i][0] == key_1:
        update_tuple = (key_2,fruit_items[i][1])
        fruit_items_copy[i] = update_tuple
print(fruit_items_copy)