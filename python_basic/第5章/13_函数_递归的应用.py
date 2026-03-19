# 使用递归求阶乘
# 特殊处理
def facto(num):
    if num == 0:
        return '的阶乘是1'
    elif num == 1:
        return '的阶乘是1'
    else:
        return factorial(num)

def factorial(num):
    if num == 0:
        print("=", end="")
        return 1
    else:
        if num != 1:
            print("*"+str(num-1),end="")
        return num * factorial(num - 1)
# 调用函数，求5的阶乘
item = 10
print(str(item)+'的阶乘:\n'+str(item),end="")
result = facto(item)
print(result)