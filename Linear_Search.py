# Implementing Linear Search using Python
# Date: 01/05/2021
# Author: Pranav H. Deo

import numpy as np


def Linear_Search(L, element):
    loc = 999999
    for index, ele in enumerate(L):
        if ele == element:
            loc = index
    return loc


# Main
MyList = np.random.randint(0, 500, 100)
print(MyList)

search_number = int(input('> Enter the Number : '))
loc = Linear_Search(MyList, search_number)
if loc != 999999:
    print('\n> Element ', search_number, ' found at location : ', loc+1)
else:
    print('\n> Element ', search_number, ' not found')
