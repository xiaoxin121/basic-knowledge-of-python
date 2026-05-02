'''
集合set
set是一种无序的、不可重复的、可修改的数据容器
定义 变量名={数据}
定义空集合 变量名=set()  空集合不可以用s={},空的{}表示字典
由于集合是无序的，所以是不支持下标索引访问的
'''



s={}
print(type(s)) # <class 'dict'>

s1={4,5,6,7}
print(type(s1)) # <class 'set'>

s2={1,2,3,4,5}
print(type(s2))
# add(...) 添加元素到集合中
# s1.add(1)
# s1.add(2)
# remove(..) 移除集合中的制定元素（制定元素不存在，将会报错）
# s1.remove(1)
# pop() 随机删除集合中的元素并返回
# s1.pop()
# clear() 清空集合
# s1.clear()
# difference(集合) 求两个集合的差值，包含在第一个集合但不包含在第二个集合的元素 也可以用-  s1-s2
s3=s1.difference(s2)
print(s3) #{6, 7}
s3=s1-s2
print(s3) #{6, 7}
# union(s2) 求两个集合的并集 |
s3=s1.union(s2)
print(s3) #{1, 2, 3, 4, 5, 6, 7}
s3=s1|s2
print(s3) #{1, 2, 3, 4, 5, 6, 7}
# intersection(s2) 求两个集合的交集 也可以使用&合并
s3=s1.intersection(s2)
print(s3) #{4, 5}
s3=s1&s2
print(s3) #{4, 5}