"""
continue 和 break 都可用于循环语句中（while 循环、for 循环都可以）
它们的作用分别是：
 continue：跳过本次循环剩余语句，直接进入下一次循环判断。
 break：立即终止循环，不再执行后续循环。
"""
# 测试continue
# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     continue
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     if day == 2:
#         continue
#     print('睡觉')

# for day in range(1, 5):
#     if day == 2:
#         continue
#     print(f'********第{day}天********')
#     print('吃饭')
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     for item in range(1, 3):
#         print(f'面包{item}')
#         continue
#         print(f'牛奶{item}')
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     for item in range(1, 3):
#         print(f'面包{item}')
#         if day == 4 and item == 2:
#             continue
#         print(f'牛奶{item}')
#     print('睡觉')

# 测试break
# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     break
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     if day == 2:
#         break
#     print('睡觉')

# for day in range(1, 5):
#     if day == 2:
#         break
#     print(f'********第{day}天********')
#     print('吃饭')
#     print('睡觉')

# for day in range(1, 5):
#     print(f'********第{day}天********')
#     print('吃饭')
#     for item in range(1,3):
#         print(f'面包{item}')
#         if day == 4 and item == 2:
#             break
#         print(f'牛奶{item}')
#     print('睡觉')
