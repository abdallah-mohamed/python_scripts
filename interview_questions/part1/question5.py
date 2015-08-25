"""
5) Show three different ways of fetching every fourth item in the list. The code
should work for lists of any size.
"""
import itertools


def get_every_nth_item_approach1(my_list, n):
    return my_list[::n]


def get_every_nth_item_approach2(my_list, n):
    it = itertools.islice(my_list, 0, None, n)
    output_list = []
    try:
        while(True):
            output_list.append(it.next())
    except StopIteration:
        pass
    return output_list


def get_every_nth_item_approach3(my_list, n):
    return [item for i, item in enumerate(my_list) if i % n == 0]


if __name__ == "__main__":
    my_list = range(100)
    print (get_every_nth_item_approach1(my_list, 4))
    print(get_every_nth_item_approach2(my_list, 4))
    print(get_every_nth_item_approach3(my_list, 4))
