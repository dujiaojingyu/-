__author__ = "Narwhale"
# from pyquery import PyQuery as pq

# html = '''<div>
#     <ul id = 'haha'>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul></div>'''
#
# doc = pq(html)
# # print(doc)
# # id等于haha下面的class等于item-0下的a标签下的span标签（注意层级关系以空格隔开）
# print(doc('#haha a .bold'))


#################################################################

from pyquery import PyQuery as pq

html = '''<div class=‘content’>
    <ul id = 'haha'>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul></div>'''

doc = pq(html)
item = doc('div ul')
# print(item)
# 我们可以通过已经查找到的标签，再此查找这个标签下面的标签
# print(item.parent())
print(item.children('.item-1'))