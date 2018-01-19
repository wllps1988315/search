# -*- coding:utf-8 -*-
def binarySearch(alist,item):
    '''
    二分查找
    :param alist:
    :param item:
    :return:
    '''
    first = 0
    last = len(alist) - 1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found