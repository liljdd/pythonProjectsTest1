# 在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法
s="my叫 %s my今年 %d 岁!" % ('小明', 10)
print(s)
print('你是%s,你%.3f岁' % ('jim', len(s)))
s.capitalize()
print(s)                    # my叫 小明 今年 10 岁!
print(s.capitalize())       # My叫 小明 今年 10 岁!

print(str.center(s,30,'*'))  # ******my叫 小明 my今年 10 岁!*******
print(s.center(30,'*'))
print(s+'x%dxx'%(len(s)))
print(s.count('my'))
print(s.endswith('岁!'))
print(s.startswith('my'))
print(s.find('今年'))     # 9  索引
print(s.find('今x年'))     # -1   找不到
# print(s.index('今x年'))  # ValueError: substring not found
s='12.3'
print(s.isalnum())      # 字母或数字
print(s.isalpha())      # 字母
print(s.isdigit())      # 数字
print(s.isdecimal())    # 十进制字符
print(s.isnumeric())    # 数字字符
'''
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
False: 汉字数字
Error: 无

isdecimal()
True: Unicode数字，，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）

'''
