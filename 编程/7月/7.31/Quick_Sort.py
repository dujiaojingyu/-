__author__ = "Narwhale"

def quick_sort(alist,first,last):
    """快速排序"""
    if first > last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        #控制左移动
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        #控制右移动
        while low < high and  alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value

    quick_sort(alist,first,low-1)
    quick_sort(alist,low+1,last)


li = [54,26,93,17,77,31,44,54,55,20]
quick_sort(li,0,len(li)-1)
print(li)