def switch_dict_keys_values(dictionary):
    # creating dictionary
    switched_dict = {}
    for key, value in dictionary.items():
        # switching values
        switched_dict[value] = key
    return switched_dict

x={"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4", "key5": "value5"}
print(switch_dict_keys_values(x))