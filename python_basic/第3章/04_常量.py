"""
在程序中一旦被赋值，就不希望被修改的量（区别于变量）。
小写单词变大写 shift+cmd+U

Python 中没有强制的常量机制
当强制对常量进行修改时，最终也能改掉，但要自觉不改，这是 Python 程序员之间的约定。
"""
ADULT_AGE = 18
MONTHS_IN_YEAR = 12
MAX_USERS = 1200
PASSING_SCORE = 60
MAX_USERS = 1300

print(ADULT_AGE, MONTHS_IN_YEAR, MAX_USERS, PASSING_SCORE)
