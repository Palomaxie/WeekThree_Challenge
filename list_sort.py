
def list_sort(lists):
    dict_list = {'evens': [], 'odds': [], 'chars': []}
    even = []
    odd = []
    char = []
    for item in lists:
        if type(item) == int and item % 2 == 0:
            even.append(item)
            dict_list['evens'] = sorted(even)

        elif type(item) == int and item % 2 != 0:
            odd.append(item)
            dict_list['odds'] = sorted(odd)

        elif type(item) == str:
            char.append(item)
            dict_list['chars'] = sorted(char)

    return dict_list


print(list_sort([4, 9, 2, 3, 5, 1, 'd', 'a', 'c', 'f']))

