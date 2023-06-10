def sub_list_with_every_other_element(lst, start_index, end_index):
    # creating list and slicing the indexes
    sub_list = lst[start_index:end_index+1:2]
    return sub_list
lst=[2,3,5,7,11,13,17,19,23,29,31,37,41]
x=sub_list_with_every_other_element(lst,2, 9)
print(x)
