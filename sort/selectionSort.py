# -*- coding:utf-8 -*-

def selectionSort(alist):
    '''
    选择排序
    :param alist:
    :return:
    '''
    for fillslot in range(len(alist) -1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot + 1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)


# Q-22: Suppose you have the following list of numbers to sort: [11, 7, 12, 14, 19, 1, 6, 18, 8, 20] which list represents the partially sorted list after three complete passes of selection sort?
# (A) [7, 11, 12, 1, 6, 14, 8, 18, 19, 20]
# (B) [7, 11, 12, 14, 19, 1, 6, 18, 8, 20]
# (C) [11, 7, 12, 14, 1, 6, 8, 18, 19, 20]
# (D) [11, 7, 12, 14, 8, 1, 6, 18, 19, 20]

[11, 7, 12, 14, 8, 1, 6, 18, 19, 20]