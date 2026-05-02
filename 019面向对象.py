"""
面向过程编程
    把一个需求分解成一系列要执行的步骤，然后按照步骤依次执行这些任务（关注的事流程、步骤）
面向对象编程
    对象可以理解为现实中具体的人/物在程序中的数字化身
    对象：属性，方法
类
    描述的是一组具有相同属性和方法的模版
对象
    对象是类的实例，基于类创建出来的实例对象
对象是由类创建出来的，创建对象的这个过程叫做对象实例化

__dict__是python中用户自定义类实例的一个特殊属性，用于以字典形式存储对象的属性
"""

# 定义类
class People:

    def __init__(self,name,age,height,weight,gender):
        """
        人员信息类
        :param name:姓名
        :param age: 年龄
        :param height: 身高
        :param weight: 体重
        :param gender: 性别
        """
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.gender=gender

    def __str__(self):
        print(f"{self.name} {self.age} {self.height} {self.weight} {self.gender}")

    def __eq__(self,other):
        """
        判断是否相等
        :param other: 要对比的对象
        :return: True or False
        """
        return self.name==other.name and self.age==other.age and self.height==other.height and self.weight==other.weight and self.gender==other.gender




# 创建对象
people = People("张三",20,200,100,"male")
people.name="张三"
people.age=18
people.height=100
people.weight=80
people.gender="male"
print(people.__dict__)

"""
魔法方法：指的是python中提供的双下划线开头和结尾的特殊方法，用于定义类的特殊行为
__init__ :初始化方法
__str__:字符串表示方法
__eq__:比较两个对象是否相等
__lt__:小于
__le__:小于等于
__gt__:大于
__ge__:大于等于
"""