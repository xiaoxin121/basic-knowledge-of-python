"""
列表的切片:
预防s:[start:end:step]
    特点:
    start:开始索引,不指定默认为0,第一个元素的索引
    end:结束索引不指定默认为列表的长度,直到列表的末尾
    step:步长,不指定默认为1
"""

# 下标1开始,下标4(不含)结束,步长1
my_list=[1,2,3,4,5]
new_list=my_list[1:4]
print(new_list)

# 从头开始,到最后结束,步长1
my_tuple=(1,2,3,4,5)
new_tuple=my_tuple[:]
print(new_tuple)

# 从头开始,到最后结束,步长2
my_list=[1,2,3,4,5]
new_list=my_list[::2]
print(new_list)

# 从头开始,到下标4(不含)结束,步长2
my_str="12345"
new_str=my_str[:4:2]
print(new_str)

# 从头(最后)开始,到尾结束,步长-1(倒序)
my_str="12345"
new_str=my_str[::-1]
print(new_str)