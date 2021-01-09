# Code: Binary Search using Python
# Date: 01/05/2021
# Author: Pranav H. Deo

def Binary_Search(L, ele, low, high):
    while low <= high:
        if low == high and ele == L[low]:
            return low
        elif low == high and ele != L[low]:
            return 99999
        elif low < high:
            mid = int((low + high) / 2)
            if ele == L[mid]:
                return mid
            elif ele < L[mid]:
                high = mid - 1
                Binary_Search(L, ele, low, high)
            else:
                low = mid + 1
                Binary_Search(L, ele, low, high)
    return 99999


# Main
MyList = [1, 4, 7, 10, 25, 48, 99, 109, 208, 297, 504, 505, 599, 609, 699, 700]
element = int(input('> Enter the Element to Search : '))
pos = Binary_Search(MyList, element, 0, len(MyList)-1)
if pos != 99999:
    print('Element Found at : ', pos)
else:
    print('Element not found')
