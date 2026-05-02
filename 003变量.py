# 变量就是存储单个数据的容器（经常会发生变化的数据）
# 一个变量存储一个值
# 变量定义的时候必须赋值才能使用
# 一条语句可以定义多个变量
# ================================================================
from types import NoneType

# 变量名=变量值
money=50
money-=10
money-=5
print(money)

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

# 判断某个变量是否是某个类型
text="nihao"
# 方法1
print(type(text)==str)
# 方法2
print(isinstance(text,str))
