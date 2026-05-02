"""
字符串是字符的容器,一个字符中可以存放任意数量的字符.比如"Python" 'Python' ''''Python''
特点:不可变性、有序性、可迭代性
字符串中的每一个字符元素都有其对应的下标（索引），通过元素对应索引就可以获取到对应的元素。
"""

# 从头开始,到下标4(不含)结束,步长2
my_str="12345"
new_str=my_str[:4:2]
print(new_str)

# 从头(最后)开始,到尾结束,步长-1(倒序)
my_str="12345"
new_str=my_str[::-1]
print(new_str)


text="Hello World"
# 字符串的不可变性
text[3]="X" # TypeError: 'str' object does not support item assignment
print(text)


"""
常用方法
find()              在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1
count()             统计子串在字符串中出现的次数
upper()             将字符串中的所有字母转换为大写
lower()             将字符串中的所有字母转换为小写
split()             将字符串按指定分隔符分割成列表
strip()             去除字符串两端的空白字符或指定字符
replace()           将字符串中的指定子串替换为新的子串
startswith()        检查字符串是否以指定子串开头，返回布尔值。
============================
s.find('Python')
s.count('H')
s.upper()
s.lower()
s.split('')
s.strip() / s.strip('*')
s.replace('H','C')
s.startswith('P')
"""

