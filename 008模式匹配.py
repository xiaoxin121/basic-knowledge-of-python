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