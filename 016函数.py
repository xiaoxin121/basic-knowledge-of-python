"""
什么是函数：函数就是组织好的、可重复使用的、用来实现特定功能的代码片段
定义函数
def 函数名(参数列表)：
    函数体
    。。。、
    return 返回值

调用函数
函数名（参数）
"""

# 定义函数
def Helloworld():
    print('Hello World!')

# 调用函数
Helloworld()

# 函数必须先定义，再调用，Python代码从上往下解释

def add(a, b):
    """
    计算两个值的加和
    :param a: 第一个值
    :param b: 第二个值
    :return: 返回加和
    """
    return a + b
def sub(a, b):
    return a - b

print(add(1, 2))
print(sub(1, 2))

# python可以返回多个值
def add_and_sub(a, b):
    return a + b,a-b

result = add_and_sub(1, 2)
print(result) #(3, -1)
print(type(result)) #<class 'tuple'>


# 如果要在函数中使用全局变量，则使用关键字 global
num=10

def update_num():
    num=100
    return num

def update_num_global():
    global num
    num=100
    return num

update_num()
print(num) # 10
update_num_global()
print(num)  # 100



# 传参方式指的是在调用函数时，传递实参的方式
# 位置参数：调用函数根据函数定义时的位置来传递参数
# 关键字参数：调用函数时以函数定义时形参名称作为关键字，以“键=值”的形式传递参数（不要求顺序） 如果位置参数与关键字混用，关键字参数必须在位置参数之后

# args代表多个参数，元组类型， **kwargs可以传关键字参数 **kwargs字典类型
def method_1(*args, **kwargs):
    print(args, kwargs)
    print(kwargs.get("count"))

method_1(1,2,3,count=4)


# 匿名函数 指的是没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写 单行表达式
# lambda 参数列表：函数体
nmMethod=lambda :print("匿名函数")
var = lambda x, y: x + y

nmMethod()
var(1,3)

# 按照字符长度排序
data_list = ["C++", "C", "Python","Jack", "PHP","Java","Go","JavaScript","Rust"]
print(data_list)
# print(type(data_list))
data_list.sort()
print(data_list)
data_list.sort(key=lambda item:len(item))
print(data_list)
data_list.sort(key=lambda item:len(item), reverse=True)
print(data_list) #翻转
