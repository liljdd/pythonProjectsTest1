import re

# re.match函数 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('www', 'www.runoob.com'))  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

print('---------------------------------------------------')
# 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式
line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    print(matchObj, type(matchObj))
    print(matchObj.groups())
else:
    print("No match!!")

print('---------------------------------------------------')
# re.search 扫描整个字符串并返回第一个成功的匹配
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

print('---------------------------------------------------')
# re.sub用于替换字符串中的匹配项
phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)

print('---------------------------------------------------')
# re.compile() 返回 RegexObject 对象
# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用
pattern = re.compile(r'\d+')
print(pattern.match('a0123adbd'))
print(pattern.search('a0123adbd').span())

print('---------------------------------------------------')
# findall(string[, pos[, endpos]])  注意： match 和 search 是匹配一次 findall 匹配所有
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

print('---------------------------------------------------')
# re.split(pattern, string[, maxsplit=0, flags=0])
# split 方法按照能够匹配的子串将字符串分割后返回列表
ll = re.split('\W+', 'runoob!runoob, runoob?')
print(ll)  # ['runoob', 'runoob', 'runoob', '']
ll = re.split('\W+', 'runoob!runoob, runoob?', 2)
print(ll)  # ['runoob', 'runoob', 'runoob?']
