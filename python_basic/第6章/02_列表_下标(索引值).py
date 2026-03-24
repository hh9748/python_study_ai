# 定义一个列表
nums = [10, 20, 30, 40, 50]

# 测试正索引。正索引：从左往右数，起始元素是 0，随后是 1，依次类推。
# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3])
# print(nums[4])

# 测试负索引   负索引：从右往左数，起始元素是 -1，随后是 -2，依次类推。
# print(nums[-1])
# print(nums[-2])
# print(nums[-3])
# print(nums[-4])
# print(nums[-5])

# 测试错误索引  注意：通过下标取值时，下标不要超出范围，否则会报错。index out of range
# print(nums[5])

# 定义一个嵌套列表
nums2 = [10, 20, ['你好啊','尚硅谷'], 40, 50]
# 取出“尚硅谷”
print(nums2[2])
print(nums2[2][1])