# 前序知识
# print('你好', end='')
# print('尚硅谷', end='')
num = 1
while num <= 9:
    num2 = 1
    while num2 <=num:
        print(f'{num2}*{num}={num*num2}',end='\t')
        num2 += 1
    num += 1
    print()

# for num in range(1,10):
#     for item in range(1,num+1):
#         print(f'{item}*{num}={num*item}',end='\t')
#     print()

