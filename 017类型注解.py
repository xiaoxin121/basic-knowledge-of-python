"""
类型注解是Python中的一种语法特性，用于明确标识变量、函数参数和返回值的数据类型，从而使代码更清晰、更安全、更易维护。
"""
# 变量定义- 未指定类型注解
a=596
score = 98.5
hobby ="Python"
flag = True
pic = None
names = ["A", "C", "E"]
phones = {"13309091111","15209101902","18809019201"}
options = {"count":2, "total":10}
goods = ("手机",6999,1)

#变量定义- 指定类型注解
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None
names2: list[str] = ["A", "C", "E"]
phones2: set[str] = {"13309091111", "15209101902", "18809019201"}
options2: dict[str, int] = {"count":2, "total":10}
goods2: tuple[str, int, int] = ("手机", 6999,1)


# 为函数添加类型注解，其实主要就是为函数的参数和返回值添加类型注解，具体语法如下:
def calc(scores: list[int]) -> float:
    """

    :param scores:
    :return:
    """
    return sum(scores)/ len(scores)