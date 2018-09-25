import sys  # 引入 sys 模块

list = [1, 2, 3, 4, 5]
it = iter(list)
print(it, type(it))

for i in it:
    print(i, end=',')
print()

# it = iter(list)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


print('=====================')


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
print(f, type(f))

# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

print('====不定长参数=======')


# 可写函数说明   加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)

print('===============')


# 加了两个星号 ** 的参数会以字典的形式导入
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)

print('=======匿名函数=======')
# python 使用 lambda 来创建匿名函数
# 语法：lambda [arg1 [,arg2,.....argn]]:expression

# 可写函数说明
mysum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", mysum(10, 20))
print("相加后的值为 : ", mysum(20, 20))


sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
