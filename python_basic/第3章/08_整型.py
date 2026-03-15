"""
调用 print(a)时，Python 底层会把 a 的类型转换成『字符串类型』再输出，而从 Python3.11
起，Python 对超大整数转换字符串的长度进行了限制，默认位数是 4300 位。
"""
# 所谓整型，就是没有小数点的数字，可以是正数，也可以是负数，也可以是0。

import sys

age = 18
temp = -15
score = 0

# 当数很大时，我们可以使用下划线将数字进行分组，来让数字变得更易读。
salary = 300_000
house_price = 3_200_000
graduates = 12_000_000
print(salary, house_price, graduates)

# Python中整数的上限值，取决于执行代码的计算机的内存和处理能力。
a = 9 ** 9999
# 以前Python版本都没有这个最大计算数限制
# 估计是为了防止拒绝服务攻击之类（如构造一个超大计算让服务器死机）所以加了一这么一个限制最大计算。
# 设置为0表示让这个不受限制
sys.set_int_max_str_digits(0)
print(a)