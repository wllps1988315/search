# -*- coding:utf-8 -*-

def bubbleSort(alist):
    '''
    冒泡排序示例
    :param alist:
    :return:
    '''
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def shortBubbleSort(alist):
    '''
    A bubble sort is often considered the most inefficient sorting method since it must exchange items before the final location is known.
    These “wasted” exchange operations are very costly. However, because the bubble sort makes passes through the entire unsorted portion of the list,
    it has the capability to do something most sorting algorithms cannot. In particular, if during a pass there are no exchanges,
    then we know that the list must be sorted. A bubble sort can be modified to stop early if it finds that the list has become sorted.
    This means that for lists that require just a few passes, a bubble sort may have an advantage in that it will recognize the sorted list and stop.
    :param alist:
    :return:
    '''
    exchanges = True
    passnum = len(alist) -1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum = passnum - 1

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

alist_short = [20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist_short)
print(alist_short)



'''Q-15: Suppose you have the following list of numbers to sort: <br> [19, 1, 9, 7, 3, 10, 13, 15, 8, 12] which list represents the partially sorted list after three complete passes of bubble sort?
(A) [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
(B) [1, 3, 7, 9, 10, 8, 12, 13, 15, 19]
(C) [1, 7, 3, 9, 10, 13, 8, 12, 15, 19]
(D) [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
正确答案:B
'''