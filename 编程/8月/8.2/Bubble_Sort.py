__author__ = "Narwhale"

def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(0,n-1):
        for i in range(0,n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]


li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)