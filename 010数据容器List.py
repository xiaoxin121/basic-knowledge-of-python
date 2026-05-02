# 什么是数据容器
# 一种可以容纳多份数据的数据类型,容纳的每一份数据称之为一个元素
# 每一个元素,可以是任意类型的数据,如字符串,数字,布尔等.
#可以分为五类:列表list  元组tuple 字符串str 集合set 字典dict

#1.列表list
# 定义列表
name_list=["张三","李四","王五"]
# 定义空列表
list1=[]
# 通过list(),定义空列表,使用比较少
list2=list()
# 反向索引:从后往前,下标从-1开始
print(name_list[-1])

# extend(数据容器),将数据容器的元素追加到列表中
name_list2=["李柳","张翼"]
name_list.extend(name_list2)
print(name_list)

#解包:将列表这一类容器解开成一个个独立的元素
newList3=[*name_list,*name_list2]
print(newList3)

newList4=name_list+name_list2
print(newList4)

# insert(下标,元素) 指定位置插入元素
name_list.insert(3,"ww")




# 删除指定元素
del name_list[2]
# .pop(下标)返回删除的这个元素
print(name_list)
#2.元组tuple
# 元组数据一旦定义不可修改,元素是有序存储的,每一个元素都有下标,可以支持任意类型的数据存储
t1=(1,2,3,4,5,6)
t2=(1,2,"1234",True)


#列表推导式->就是按照一定的规则快速生成一个列表的方法:语法格式:[要插入的值 for i in 序列/列表]
#举例生成1-20的平方
#正常操作
tdsList=[]
for item in range(1,21):
    tdsList.append(item**2)
print(tdsList)
#推导式
tdslist2=[item**2 for item in range(1,21) ]
print(tdslist2)
