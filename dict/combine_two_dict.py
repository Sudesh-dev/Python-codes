# combine two dictionaries and print the combined dictionary.
def convert_to_dict(keys_dict,values_dict):
    new_dict={}
    for i in range(len(keys_dict)):
        key=keys_dict[i]
        value= values_dict[i]
        new_dict[key]=value
    return new_dict

def convert_to_int(values):
    new_list = []
    for i in values:
        num = int(i)
        new_list.append(num)
    return new_list

dict_1_keys = input().split()
dict_1_values= input().split()
dict_2_keys = input().split()
dict_2_values= input().split()

dict_1_values = convert_to_int(dict_1_values)
dict_2_values = convert_to_int(dict_2_values)

dict_1 = convert_to_dict(dict_1_keys,dict_1_values)
dict_2 = convert_to_dict(dict_2_keys,dict_2_values)

dict_1.update(dict_2)
dict_items = dict_1.items()
dict_items = sorted(dict_items)
print(dict_items)

