# 1.迭代器是惰性计算，不会一次性生成所有结果，所以能显著降低内存占用。
# 2.当数据量很大，不确定要用多少结果时，推荐使用迭代器。

import tracemalloc


# 使用迭代器实现 非波拉切数列
class Fibo:
    def __init__(self, total):
        # 维护总数
        self.total = total
        # 维护指针位置
        self.__index = 0
        # 维护用于计算的两个数
        self.pre = 1
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.total == 0:
            value = []
            self.total = -1
            return value
        if self.__index >= self.total:
            raise StopIteration
        # 前两个数是1
        if self.__index < 2:
            value = 1
        # 从第三个数开始每一个数都是前两个数的和
        else:
            value = self.pre + self.cur
        # 更新迭代器的状态
        self.__index += 1
        # 更新需要迭代的数
        self.pre = self.cur
        self.cur = value
        return value
#
#
# f1 = Fibo(0)
# for item in f1:
#     print(item)


# 不使用迭代器
def fibo(total):
    if total <= 0:
        return []
    if total == 1:
        return [1]
    nums = [1, 1]
    for total in range(2, total + 1):
        nums.append(nums[-1] + nums[-2])
    return nums

tracemalloc.start()
f1 = Fibo(100000)
print(f'内存占用是:{tracemalloc.get_traced_memory()[1]/1024/1024}MB')

# tracemalloc.start()
# f2 = fibo(100000)
# print(f'内存占用是:{tracemalloc.get_traced_memory()[1]/1024/1024}MB')
