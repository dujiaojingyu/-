__author__ = "Narwhale"


def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n//2
    while gap > 0:
        for j in range(gap,n):
            for i in range(j,0,-1):
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                else:
                    break
        gap = gap // 2


def shell_sort1(alist):
    """希尔排序"""
    n = len(alist)
    gap = n//2
    while gap > 0:
        for j in range(gap,n):
            i=j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                else:
                    break
        gap = gap // 2




li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
li1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(li)
shell_sort1(li1)
print(li)
print(li1)
