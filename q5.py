def compare_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    common_elements = list(set1.intersection(set2))
    non_common_elements = list(set1.symmetric_difference(set2))

    return common_elements, non_common_elements

list1=["One Punch Man","Attack On Titan","One Piece","SwordArt Online","Bleach","Dragon Ball Z","One Piece"]
list2=[ "Full Metal Alchemist","Code Geass","DeathNote","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]

print(compare_lists(list1,list2))
