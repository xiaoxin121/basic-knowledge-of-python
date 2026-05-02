"""
Python模块(module):一个.py文件就是一个模块，模块是Python程序的基本组织单位。在模块中可以定义变量、
函数、类，以及可执行的代码

import 模块名                           import random,os                                   模块名.功能名                 random.randint(10,100)
import 模块名 as 别名                    import random as rd                                 别名.功能名                  rd.randint(10, 100)
from 模块名 import 功能名                from random import randint,choice                    功能名                     randint(10,100)
from 模块名 import 功能名 as 别名         from random import randint as rint                 别名                         rint(10, 100)
from 模块名 import *                    from random import *                               功能名                      randint(10, 100)
"""
# import Module.SimpleCalculation as Sc
from utils import  *
# from utils.Module1 import *

print(Module1.add(1,2,3,4,5,6,7,8,9,10))

#测试函数:
# __name__:Python中内置变量，表示的当前模块的名字(直接运行当前模块，__name__的值为__main__;当该模块被导入时，name__的值就是模块名称
# __all__是一个模块级别的特殊变量，用于指定from 模块名 import * 时会导入哪些功能(*通配了哪些功能)。


"""
导入包的所有方法
当你使用from package import *时，你会导入包中的所有公开方法和属性。这种方式的好处是方便，因为你不需要记住所有方法的名字，可以直接使用。然而，这种方式也有缺点：

‌命名空间污染‌：这可能会导致命名冲突，特别是当两个包中有相同名称的方法时。
‌效率问题‌：虽然在大多数情况下，这种方式的性能损耗非常小，但如果导入的模块非常大，或者在频繁导入的情况下，可能会有微小的性能影响。
2. 导入包指定的方法
使用from package import specific_method来导入特定的方法。这种方式的好处是：

‌清晰性‌：代码更清晰，每个导入的方法都有一个明确的名称。
‌避免命名冲突‌：减少了命名冲突的风险。
‌性能‌：在大多数情况下，这种方式比导入所有内容要快一些，因为Python只需要加载和绑定你实际使用的那些名称。
性能比较
在大多数现代Python实现（如CPython）中，这两种方式的性能差异非常小，以至于在实践中通常可以忽略不计。然而，如果你在性能敏感的应用中工作（例如，实时系统或高频交易系统），你应该考虑以下几点：

‌模块加载时间‌：虽然单个方法的导入通常更快，但如果模块非常大或包含复杂的初始化代码，首次导入时可能会有显著差异。
‌重复导入‌：如果代码被频繁执行（例如，在循环中），重复导入同一个模块的所有内容可能会导致额外的开销。相比之下，重复导入特定的方法通常开销更小。
最佳实践
‌对于小型项目或日常开发‌：使用from package import *可能更方便，尤其是在快速原型开发阶段。
‌对于大型项目或生产环境‌：推荐使用from package import specific_method来明确指定需要的方法，这样可以避免潜在的命名冲突并提高代码的清晰度。
‌模块封装‌：如果模块非常大，考虑将功能封装到子模块中，然后从父模块中导入需要的子模块。例如，from package.submodule import method。
总之，虽然在实际应用中两者的性能差异不大，但推荐使用明确的导入方式来提高代码的清晰度和可维护性。在考虑性能问题时，除非有明确的性能瓶颈指向导入操作，否则通常不需要过分担心这种差异。
"""