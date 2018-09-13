# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 100:
    print(b, end=',')
    a, b = b, a + b  # 计算右边表达式，然后同时赋值给左边
print()
print("=============")
del a, b
a, b = 1, 0
while a <= 100:
    a, b = a + 1, b + a
print(b)

# print()
# print("=====while 循环使用 else 语句========")
# del a, b
# a, b = 0, int(input('请输入：'))
# while a < b:
#     a += 1
#     if a == 3: continue
#     print(a, end=',')
#     if a >= 4: break
# else:
#     print()
#     print('===', a, '===', b)

del a, b
print()
a = 'woshishui?'
for i in a:
    print(i, end=',')
else:
    print()
    print('结束了')

del a
a = range(1, 10)
print(a, type(a))
for i in a:
    print(i, end=',')

print()
print('----')
a = range(10)
for i in a:
    print(i, end=',')
# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age < 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄: ", human)
#
# ### 退出提示
# input("点击 enter 键退出")
