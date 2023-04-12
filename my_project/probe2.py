from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):

    if by_values:
        for key, val in sorted(ordered_dict.items(), key=lambda x: x[1]):
            ordered_dict.move_to_end(key)
    else:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)



data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data, by_values=True)



