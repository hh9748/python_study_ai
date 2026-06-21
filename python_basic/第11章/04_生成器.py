# 1️⃣生成器：
#   1.生成器函数：函数体中如果出现了 yield 关键字，那该函数是『生成器函数』。
#   2.生成器对象：调用『生成器函数』时，其函数体不会立刻执行，而是返回一个『生成器对象』。
#   备注：不管能否执行到 yield 所在的位置，只要函数中有 yield 关键字，那该函数，就是『生成器函数』。
# region
# def demo():
#     print('demo函数执行了')
#     print(100)
#     yield
#     a = 200
#     print(a)
#
#
# d = demo()
# print(d)
# endregion
from multiprocessing.reduction import sendfds

# 2️⃣写在『生成器函数』中的代码，需要通过『生成器对象』来执行：
#   1.调用『生成器对象』的 __next__ 方法，会让『生成器函数』中的代码开始执行。
#   2.当『生成器函数』中的代码开始执行后，遇到 yield 会“暂停”执行，并且其内部会记录“暂停”的位置。
#   3.后续调用 __next__ 方法时，都会从上一次“暂停”的位置，继续运行，直到再次遇到 yield。
#   4.遇到 return 会抛出 StopIteration 异常，并将 return 后面的表达式，作为异常信息。
#   5.yield 后面所写的表达式，会作为本次 __next__ 方法的返回值。
# region
# def demo2():
#     print('demo函数执行了')
#     print(100)
#     yield '我是第一个yield返回的数据'
#     a = 200
#     print(a)
#     yield '我是第二个yield返回的数据'
#     b = 300
#     print(b)
#     yield
#     return "异常信息"
#
#
# d = demo2()
# r1 = next(d)
# print(r1)
# r2 = next(d)
# print(r2)
# r3 = next(d)
# print(r3)
# try :
#     next(d)
# except StopIteration as e:
#     print(e)
# endregion

# 3️⃣生成器对象是一种特殊的迭代器（本质是通过 yield 自动实现了迭代器协议）。
# region
# def demo3():
#     print('demo函数执行了')
#     print(100)
#     yield '我是第一个yield返回的数据'
#     a = 200
#     print(a)
#     yield '我是第二个yield返回的数据'
#     b = 300
#     print(b)
#     return "异常信息"
#
# # 验证：生成器对象的__iter__方法，和迭代器一样，返回的也是自身
# d = demo3()
# # print(hasattr(d, '__iter__'))
# # print(d == iter(d))
# # print(hasattr(d, '__next__'))
#
# # for item in d:
# #     print(item)
#
# # for循环背后的逻辑
# it = iter(d)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break
# endregion

# 4️⃣yield 也能写在循环里
# region
# def create_car(total):
#     for index in range(1, total + 1):
#         yield f'我是第{index}台车'
#
#
# cars = create_car(10)
# for car in cars:
#     print(car)
# endregion

# 5️⃣yield from 能把一个『可迭代对象』里的东西依次 yield 出去。(替代：for + yield)
# region
# def demo():
#     nums = [10, 20, 30, 40, 50]
#     yield from nums
#
#
# for num in demo():
#     print(num)
# endregion

# 6️⃣使用：生成器.send(值) 可以让生成器继续执行的同时，给上一次 yield 传值。
# 备注1：next 只能取值，send 既能取值，也能送值
# 备注2：第一次启动生成器，不能传值！
# region
# def demo3():
#     print('demo函数执行了')
#     print(100)
#     a = yield '我是第一个yield返回的数据'
#     print(a)
#     b = yield '我是第二个yield返回的数据'
#     print(b)
#     return "异常信息"
#
# d = demo3()
# print(d.send(None))
# r1 = d.send(666)
# print(r1)
# try:
#     r2 = d.send(888)
#     print(r2)
# except StopIteration as e:
#     print(e)
# endregion


# 用生成器实现遍历Person类的实例对象
# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         self.__attr = [name, age, gender, address]
#
#     def __iter__(self):
#         # yield self.name
#         # yield self.age
#         # yield self.gender
#         # yield self.address
#         yield from self.__attr
#
# p1 = Person('张三', 18, '男', '北京昌平')
#
# for item in p1:
#     print(item)
# endregion


# 用生成器实现斐波那契数列
# region
# def fibo(total):
#     per = 1
#     cur = 1
#     for index in range(total):
#         if index < 2:
#             yield 1
#         else:
#             value = per + cur
#             per = cur
#             cur = value
#             yield value
# # f1 = fibo(10)
# # for item in f1:
# #     print(item)
#
# # 无论是迭代器，还是生成器对象，都可以用list、tuple、set等直接拿到其里面的所有内容（注意：容易挤爆内存）
# f1 = list(fibo(100))
# print(f1)
# endregion


# 生成器表达式：一种用类似列表推导式的语法，快速创建生成器对象的方式。
# 语法格式：(表达式 for 变量 in 可迭代对象)
# 什么时候适合用生成器表达式？———— 当“每个结果，只依赖当前这一个元素”时。
# region
# nums = [10, 20, 30, 40]
#
# # 列表推导式
# result = [n * 2 for n in nums]
# print(result)
#
# # 生成器推导式
# result2 = (n * 2 for n in nums)
# for n in result2:
#     print(n)
# endregion
