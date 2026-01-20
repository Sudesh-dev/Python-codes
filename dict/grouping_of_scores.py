# group the scores of the students and print the grouped scores.

def get_dict(items):
    new_dict={}
    for i in items:
        item_list= i.split(":")
        keys,values = item_list[0], int(item_list[1])
        if keys in new_dict:
            score = new_dict[keys]
            new_dict[keys] = score + values
        else:
            new_dict[keys]= values
    return new_dict
items = input().split(",")
score_pairs =  get_dict(items)
score_items = score_pairs.items()
score_items = sorted(score_items)

print(score_items)
