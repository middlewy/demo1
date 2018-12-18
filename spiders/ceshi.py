# from lxml import etree
# import copy
# from scrapy.cmdline import execute
# execute(['scrapy','crawl','lol'])


# html = etree.HTML(response.text)

# a = [1,2,3,[1,2]]
# # b = copy.deepcopy(a)
# b = copy.copy(a)
# a.append(4)
# print(b)
# print(a)

#有一个列表lista，请使用map()函数输出它的平方，并使用列表推导式提取出大于10的数
# def pingfang(*args):
#     lista = list(args)
#     s = map(lambda x:x ** 2,lista)
#     a = [i for i in s if i >10]
#     return a
#
# def Sum(func):
#     print('它们的和是：')
#     print(sum(func))
#
#
# if __name__ == '__main__':
#     a = Sum(pingfang(1,2,3,4))

#去除列表中的重复元素
# lista = []
# L = ['b','c','d','c','b','a','a']
# for i in L:
#     if i in lista:
#         pass
#     else:
#         lista.append(i)
# print(lista)


#从小到大排序
# lista = [2,5,4,3,9,6]
# listb = []
# for i in range(len(lista)):
#     listb.append(min(lista))
#     lista.remove(min(lista))
# print(listb)

#请用一行代码将 s = 'info:xiaozhang 33 shandong'切分成列表输出
# import re
# s = 'info:xiaozhang 33 shandong'
# a = re.split(r':| ',s)
# print(a)

# 求101到200间的素数
# lista = []
# for i in range(101,200):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         lista.append(i)
# print(lista)


#利用递归函数调用方式求1到10的和。
# def sum(x):
#     if x == 1:
#         return x
#     else:
#         return sum(x-1) + x
#
# print(sum(6))









