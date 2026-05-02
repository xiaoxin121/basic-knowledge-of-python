# Python基础知识

### 001注释

分为单行注释和多行注释

```python
# 1.单行注释 使用#号
# money=50
# money-=10
# money-=5

# 2.多行注释
"""
money=50
money-=10
money-=5
"""
```

### 002标识符

是程序员在代码中为变量、函数、类等元素所起的名字

命名规则：

​	1.只能包含字母（a-z,A-Z） 数字(0-9) 下划线(_)

​	2.不能以数字开头

​	3.不能使用关键字 True False None and or if else for 等

​	4.严格区分大小写,比如:age,Age,AGE是三个变量

```python
# 1str1="hello"  不合法
# str1="hello"  合法
# str_1="hello" 合法
# _str1="hello" 合法
# __str1="hello" 合法
# True="hello" 不合法
# A1="hello" 合法
```

### 003变量

程序中用来存储单个数据的容器，通常会把经常发生的数据存储在变量中。

语法：

​		变量名=变量值 

规则：

​	1.一个变量存储一个值

​	2.变量定义的时候必须赋值才能使用

​	3.一条语句可以定义多个变量

```python
from types import NoneType

# 变量名=变量值
money=50
print(money)

# 一次定义多个参数变量
num1,num2=1,2
print(num1)
print(num2)

# 数据类型
# int  整型
# float 浮点型
# str 字符串
# bool 布尔类型
# NoneType 空值:表示空或无值,仅包含一个值None
# 可通过 isinstance()检查数据是否属于制定的类型,返回的是一个bool值

# 定义变量的存储分数
score=90 #
print(type(score))
height=1.87
print(type(height))
is_marry=False
print(type(is_marry))
name="张三"
print(type(name))

# 输出
# 35
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'str'>

# 判断某个变量是否是某个类型
text="nihao"
# 方法1
print(type(text)==str)
# 方法2
print(isinstance(text,str))

```

注：Python是动态类型语言，在程序运行时，才进行类型检查，变量的类型可以在程序运行过程中改变，一个变量可以接收不同类型的值。

### 004字符串的定义和拼接

#### 	一、字符串的三种定义方式

```python
text1 = "这是字符串的第一种定义方式：使用双引号"
text2 = '这是字符串的第二种定义方式：使用单引号'
text3 = '''
这是字符串的第三种定义方式：
使用三个单引号
可以接受换行
'''
```

#### 二、带转义字符的字符串定义

```python
# 方式1：单引号和双引号交替使用
text1 = "这是单引号'"
text1 = '这是双引号"'
# 方式2：使用转义\
text1 = '这是单引号\''
text1 = "这是双引号\""
```

#### 三、字符串拼接

```python
# 方式1
str1= "hello" "world"
print(str1)

# 方式2
str2="hello"+"world"
print(str2)
str3=str1+str2
print(str3)

# int类型转string类型
age=10
print(type(str(age)))
```

四、字符串格式化

```python
# 通过%占位符的形式完成字符串和变量的快速拼接
print("大家好,我是%s,我今年%d岁了" % ("张三",age))
# 也可以通过 f"内容{变量/表达式}“的形式来完成快速格式化
name="李四"
print(f"大家好,我是{name},我今年{age}岁了")
```

### 005输入输出

input()的功能就是获取键盘输入的数据,具体用法为：s=input("提示信息")
print()的功能就是将数据输出到控制台,具体用法为：print(数据)

```python
s=input("请输入你的姓名！")
print(s)
```

### 006运算符

可以分为算术运算符、赋值运算符、比较运算符、逻辑运算符

```python
# 算术运算符
# + 加
# - 减
# * 乘
# / 除
# // 取整除
# % 取余
# ** 指数:a**b为a的b次方
# 算术符的优先级  ** => % // / * => + -

print("10/3=", 10 / 3)
print("10//3=", 10 // 3)
print("10.0//3=", 10.0 // 3)
print("10%3=", 10 % 3)
print("10**3=", 10 ** 3)
#
# 输出结果
# 10/3= 3.3333333333333335
# 10//3= 3
# 10.0//3= 3.0
# 10%3= 1
# 10**3= 1000

# 赋值运算符=
# 同时给多个变量赋值
name, age, height = "zs", 10, 20
# 多个变量赋相同的值
a = b = 3

#
# 复合运算符
# +=
# -=
# *=

# 比较运算符:
# ==  判断a是否等于b
# !=  判断a是否不等于b
# >   判断a是否大于b
# <
# >=
# <=

# 逻辑运算符
# and
# or
# not
```

### 007if判断逻辑

```python
# 基本用法
# 只有满足指定条件,才会执行对应的代码逻辑
# if 判断条件：
#     需要执行的代码逻辑

age = int(input("请输入您的年龄!"))

if age >= 18:
    print("您的年龄为%s,成年了可以进入" % age)
elif age >= 16:
    print(f"您{age}了")
else:
    print("结束了")
```

### 008模式匹配

```python
'''
模式匹配 match...case
结构模式匹配就是用一个清晰的模版去精准的匹配数据的结构和内容,匹配成功则执行响应的操作
match 表达式:
    case 值1:
        操作1
    case 值2 if条件表达式:
        操作2:
    case 值3 | 值4: 匹配3或匹配4
        操作3
    case _:
        其他情况的操作
'''

num=int(input("今天星期几?"))

match num:
    case 1:
        print("星期一:要去上班.")
    case 2:
        print("星期二:去上班")
    case 3:
        print("星期三:要去上班")
    case 4:
        print("星期四:要去学习")
    case 5:
        print("星期五:快要星期了")
    case 6:
        print("星期六:放假了")
    case 7:
        print("星期天:真无聊")
    case _:
        print("不想上班")
```

### 009循环

```python
'''
1.while循环： else语句可以不加
while 逻辑判断：
    需要执行的逻辑1
else :
    需要执行的逻辑2

2.for循环： else语句可以不加
for num in range(10):
    需要执行的逻辑1
else:
    需要执行的逻辑2

3.range()用法
1.从0到传入的值
range(2):0,1,2
2.从开始值到结束值，每步为1
range(2,5):2,3,4,5
3.从开始值到结束值，每步为step
range(2,10,2):2,4,6,8,10
'''
num1 = 1
while num1 <= 10:
    num2 = 1
    while num2 <= num1:
        print(f"{num1}*{num2}={num1 * num2}", end="\t")
        num2 += 1
    print("")
    num1 += 1


print("="*20)

for i in range(2):
    print(i)

print("="*20)

for i in range(2,5):
    print(i)

print("="*20)



for i in range(2,10,2):
    print(i)

"""
输出：
1*1=1   
2*1=2   2*2=4  
3*1=3   3*2=6  3*3=9  
4*1=4   4*2=8  4*3=12 4*4=16 
5*1=5   5*2=10 5*3=15 5*4=20 5*5=25 
6*1=6   6*2=12 6*3=18 6*4=24 6*5=30 6*6=36 
7*1=7   7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49 
8*1=8   8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64 
9*1=9   9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81 
10*1=10 10*2=20    10*3=30    10*4=40    10*5=50    10*6=60    10*7=70    10*8=80    10*9=90    10*10=100  
====================
0
1
====================
2
3
4
====================
2
4
6
8
"""
```

### 010数据容器List

```python
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
```

### 011数据容器的切片

```python
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
```

### 012数据容器str

```python
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
```

### 013数据容器tuple

```python
"""
元组一旦形成，不可修改
元组是不可变的序列，类似于列表，但创建后不可改变
定义：变量名=() 或者 变量名=tuple()

组包：
拆包：


"""
tp=("123",1,2,True,"456")

print(tp.count(1))
# 是否包含
print(tp.__contains__(1))

print("========================")
# 拆包
a,b,c,d,e=("123",1,2,True,"456")
print(a)
print(b)
print(c)
print(d)
print(e)
print("========================")
# 第二种方式 *号代表其他信息
first,*other,last=tp
print(first)
print(*other)
print(last)
```

### 014数据容器set

```python
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
```

### 015数据容器dict

