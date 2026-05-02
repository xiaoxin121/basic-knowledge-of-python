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
    print("滚")

    # 案例需求
    # 定义一个数字(1~10，随机产生)，通过3次判断来猜出来数宁
    # *案例要求
    # 1.数字随机产生，范围1 - 10
    # 2.有3次机会猜测数字，通过3层嵌套判断实现
    # #3.每次猜不中，会提示大了或小了
    # * 提示
import random
num=random.randint(1,10)
print(num)
for i in range(3):
    print("请输入数字")
    result = int(input())
    if result==num:
        print("恭喜你猜对了")
        break
    elif result>num:
        print("猜大了")
    else:
        print("猜小了")

print("游戏结束")



#3)判断一个年份是否是闰年，闰年的条件是符合下面二者之一:(1)年份能被4整除，但不能被100整除:(2)能被400 整除