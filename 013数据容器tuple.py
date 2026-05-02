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


