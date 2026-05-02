"""
字典：
字典（dict)存储的是键值对（key:value)形式的数据
特点：键值对、key是唯一的，可修改
定义字典
字典名称：{key:value,key:value}
定义空字典
字典名称={}
字典名称=dict()
根据key获取value
值=字典名称[key]
注：value可以是任意类型，而key必须是不可变类型（不能为list、set、dict)
    字典内的key不允许重复、如果重复定义，后面的覆盖前面的
    字典是没有索引下标的，不能根据索引获取值，只可以根据key获取value
"""
dict={"张三":78,"李四":100,"赵六":200}
# 添加 字典名称[key]=value 往指定字典中添加key-value键值对
dict["孙七"]=50
print(dict)
# 字典名称.pop(key)         删除字典中指定的key ，并返回该key对应的vaLue
dict.pop("孙七")
print(dict)
# del 字典名称[key]                删除字典中指定的键值对
del dict["赵六"]
print(dict)
# 字典名称[key] = vatue            修改字典中指定的key对应的值
dict["赵六"]=100
print(dict)
# 字典名称[key]                    根据key获取vatLue
print(dict["张三"])
# 字典名称.get(key)                  根据key获取vaLue
print(dict.get("李四"))
# 字典名称.keys()                    获取所有的key
print(dict.keys())
# 字典名称.vaLues()                   获取所有的vaLue
print(dict.values())
# 字典名称.items()                获取所有的key-vatLue键值对
print(dict.items())