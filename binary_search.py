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

def binarySearch(alist, item):
    '''
    二分查找recursive version
    :param alist:
    :param item:
    :return:
    '''
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
          return True
        else:
          if item<alist[midpoint]:
            return binarySearch(alist[:midpoint],item)
          else:
            return binarySearch(alist[midpoint+1:],item)

if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))