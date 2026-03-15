#coding=UTF-8
"""
在该文件中，我主要学习了注释相关的内容
Python 官方建议：在#和注释的内容之间加一个空格，在代码和#之间加两个空格。
多行注释本质是一个多行字符串。
注意：Python 中并没有真正的多行注释语法，所谓多行注释的本质其实还是字符串。
"""

# name是张三的名字
name = '张三'
# age是张三的年龄
age = 18
# weight是张三的体重（单位：kg）
# 张三的体重还可以
weight = 65.2

print(name, age, weight)  # 下面是一句打印

"""
下面是一些常量
ADULT_AGE是法定成人年龄
MONTHS_IN_YEAR是一年中的几个月
MAX_USERS是最大同时在线人数
"""
ADULT_AGE = 18
MONTHS_IN_YEAR = 12
MAX_USERS = 1200
print(ADULT_AGE,MONTHS_IN_YEAR,MAX_USERS)