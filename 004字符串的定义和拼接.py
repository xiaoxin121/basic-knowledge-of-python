# 一.三种定义方式
text1 = "这是字符串的第一种定义方式：使用双引号"
text2 = '这是字符串的第二种定义方式：使用单引号'
text3 = '''
这是字符串的第三种定义方式：
使用三个单引号
可以接受换行
'''

print(type(text1))
print(type(text2))
print(type(text3))

# 运行结果
# <class 'str'>
# <class 'str'>
# <class 'str'>

# 二.带转义字符的字符串定义
# 方式1：单引号和双引号交替使用
text1 = "这是单引号'"
text1 = '这是双引号"'
# 方式2：使用转义\
text1 = '这是单引号\''
text1 = "这是双引号\""

# 三.字符串拼接
# 1
str1= "hello" "world"
print(str1)

# 2
str2="hello"+"world"
print(str2)
str3=str1+str2
print(str3)

# int类型转string类型
# str():将数据转换为字符串
# int():将数据转换为int类型
# float():将数据转换为float类型
# bool():将数据转换为bool类型

age=10
print(type(str(age)))

# 四.字符串格式化
# 通过%占位符的形式完成字符串和变量的快速拼接
print("大家好,我是%s,我今年%d岁了" % ("张三",age))
# 也可以通过 f"内容{变量/表达式}“的形式来完成快速格式化
name="李四"
print(f"大家好,我是{name},我今年{age}岁了")
