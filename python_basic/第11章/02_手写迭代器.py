# 迭代器是一次性的，状态只会向前推进，且不会自动重置（迭代器在遍历的过程中会被“消耗”）。
# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#
#     def __iter__(self):
#         return PersonIterator(self)
#
# class PersonIterator:
#     def __init__(self, person):
#         # 保存外部传入的数据
#         self.person = person
#         # 用于迭代的下标--并设置迭代器的初识状态(指针位置)
#         self.__index = 0
#         # 用于迭代的对象
#         self.__attrs = [person.name, person.age, person.gender, person.address]
#
#     # __iter__用于返回迭代器本身
#     def __iter__(self):
#         return self
#
#     # 调用next方法会根据当前迭代器的状态，返回下一个元素
#     def __next__(self):
#     # 判断当前的下标是否超过范围
#         if self.__index >= len(self.__attrs):
#             # 抛出异常
#             raise StopIteration
#         #拿到当前数据值
#         value = self.__attrs[self.__index]
#         # 更新迭代器状态(指针位置)
#         self.__index += 1
#         # 返回当前迭代的数据
#         return value
# # 目标
# p1 = Person('张三', 18, '男', '浙江省杭州市')
#
# for item in p1:
#     print(item)
# endregion

# 需求：让for循环可以遍历Person的实例对象
# 实现方式1️⃣

#         # 保存好外部传入的数据

#         # 设置迭代器的初始化状态

#         # 准备好要遍历的内容

#
#     #迭代器的iter方法返回迭代器自身
#     def __iter__(self):
#         return self
#
#     # 每次去调用next方法，会根据当前状态返回下一个元素(核心逻辑)
#     def __next__(self):
#         if self.index >= len(self.attrs):
#             #超出迭代器返回会抛出异常
#             raise StopIteration
#         # 返回下一个元素的内容
#         attr = self.attrs[self.index]
#         #更新迭代器位置
#         self.index += 1
#         return attr
#
# # 目标
# p1 = Person('李四', 18, '男', '北京市朝阳区')
#
# for item in p1:
#     print(type(item))
#     print(item)

# endregion

# 实现方式2️⃣
# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         self.__index = 0
#         self.__attrs = [name, age, gender, address]
#
#     def __iter__(self):
#         # 每次遍历的时候需要还原状态（指针位置）
#         self.__index = 0
#         return self
#
#     # 调用next方法会根据当前迭代器的状态，返回下一个元素
#     def __next__(self):
#     # 判断当前的下标是否超过范围
#         if self.__index >= len(self.__attrs):
#             # 抛出异常
#             raise StopIteration
#         #拿到当前数据值
#         value = self.__attrs[self.__index]
#         # 更新迭代器状态(指针位置)
#         self.__index += 1
#         # 返回当前迭代的数据
#         return value
#
#
# # 目标：
# # 下面的p1既是可迭代对象，又是迭代器
# p1 = Person('张三', 18, '男', '北京昌平')
#
# for item in p1:
#     print(item)
#
# for item in p1:
#     print(item)
# endregion

# 进阶：迭代器玩的就是__next__
from cn2an import an2cn
class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.__index = 0
        self.__attrs = [name, age, gender, address]

    def __iter__(self):
        # 每次遍历的时候需要还原状态（指针位置）
        self.__index = 0
        return self

    # 调用next方法会根据当前迭代器的状态，返回下一个元素
    def __next__(self):
        # 判断当前的下标是否超过范围
        if self.__index >= len(self.__attrs):
            # 抛出异常
            raise StopIteration
        # 拿到当前数据值
        value = self.__attrs[self.__index]
        # 字符串英文为大写
        if isinstance(value, str):
            value = value.upper()
        # 数字变成汉语形式
        if isinstance(value, int):
            value = an2cn(value)
        # 更新迭代器状态(指针位置)
        self.__index += 1
        # 返回当前迭代的数据
        return value
# # 目标：
# # 下面的p1既是可迭代对象，又是迭代器
# 字符串英文为大写
p1 = Person('zhangsan', 18, '男', '北京昌平')

for item in p1:
    print(item)
