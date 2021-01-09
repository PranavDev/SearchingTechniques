# Code: Jump Search using Python
# Date: 01/06/2021
# Author: Pranav H. Deo

import numpy as np


def JumpSearch(L, jump, ele):
    flag = 0
    for i in range(0, len(L)):
        if ele == L[i]:
            return i
        if ele < L[i]:
            i -= 1
            while i != -1:
                if ele == L[i]:
                    return i
                else:
                    flag = -1
                    i -= 1
            if flag == -1:
                return 99999
        else:
            i += jump


# Main
MyList = sorted(np.random.randint(0, 500, 100))
print(MyList)
# MyList = [1, 2, 5, 10, 15, 18, 34, 39, 44, 59, 60, 66, 100]
JS = int(input('> Enter Jump Size : '))
Element = int(input('> Enter Element to Search : '))
indx = JumpSearch(MyList, JS, Element)

if indx != 99999:
    print('Element Found at Pos : ', indx+1)
else:
    print('Element Not Found')
