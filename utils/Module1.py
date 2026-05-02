
def add(*args:float)->float:
    """
    计算加和
    :param args:传入的数值
    :return: 返回和 float
    """
    return sum(args)



# 执行当前文件，则会执行以下代码，如果被当做模块导入，则不会执行当前代码
if __name__ == '__main__':
    var=add(1,2,3,4,5)
    print(var)
