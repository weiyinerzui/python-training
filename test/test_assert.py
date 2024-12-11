# assert 语句的用法
# 在条件为 True 时，继续执行，在条件为 False 时，抛出 AssertionError 异常。
# 基本语法： assert condition message ，conditon 为条件语句，message为可选参数，在断言失败时显示信息

x = 5
assert x == 5, "x should be 5"
print('test pass')

# y = 10
# assert y < 5 ,"y should be less than 5"
# print('This will not be printed.')

# 在函数中使用断言
def divide(a, b):
    assert b != 0, "cannot  divide zero"
    return a / b

result = divide(10, 2) # 正常运行
print(result)

# result = divide(10, 0) # 断言失败
# print(result)

