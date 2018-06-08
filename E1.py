"""
Given an array of integers [a0, a1, ..., an] (1<=ai<=100) determine which is the most popular number. 

Most popular number appears more times that the others into given array.

If two numbers are equal of popularity algorith must return the minor of them.

Ej: [1, 3, 5, 6, 3, 6, 7, 8, 9, 6] => 6 (six is the most popular number)

"""

import collections


def popular(l):
    item_popular = collections.Counter(l).most_common()[:2]
    first_most_popular, second_most_popular = item_popular
    if first_most_popular[1] == second_most_popular[1] and first_most_popular[0] > second_most_popular[0]:
        return second_most_popular[0]
    return first_most_popular[0]


lista = [1, 3, 5, 6, 3, 6, 7, 8, 9, 6]
print("{} is the most popular.".format(popular(lista)))
