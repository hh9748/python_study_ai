"""
None 出现最多的两个场景：
  1函数中没有写 return，或写了 return 但没有返回任何内容 。
  2变量定义时，暂时还不知道要存放什么，可以先赋值为 None。
"""
# None是一个特殊的字面量，它表示：空值 / 无值 / 无意义。
msg = None

# None 的类型是 NoneType。
print(type(msg))

# None 转为布尔值是 False。
print(bool(msg))
if not msg:
    print('你好')

# 不能参与数学运算，也不能与字符串拼接。
# result1 = msg + 1
# result1 = msg + 'hello'

# 不给函数设置返回值，那函数默认就会返回 None

