#import keyword
#keyword.kwlist

# 注释
print('尾部注释') #尾部注释
'''
print('多行注释')
print('多行注释') #尾部注释
print('多行注释')
print('多行注释')
'''


"""
关键字
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

if True:
    print('keyword true')
else:
    print("xxx")

#多行语句 反斜杠\
a="aaa"
b='bbb'
c='ccc'
d=a+b+c
print(d)
e='aaa'+ \
  'bbb'+\
  'ccc'
print("e="+e)

f=["aaa","bbb",
   "ccc"]
