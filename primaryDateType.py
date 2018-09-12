# Number数据类型
print('# Number数据类型')
a,b,c,d=2,2.2,True,4+3j
print(type(a),type(b),type(c),type(d))
print(isinstance(a,int),isinstance(b,float),isinstance(c,bool),isinstance(d,complex))
## bool类型可以和数字相加
print(a+c)

del a,b,c,d
print()

# String 数据类型
print('#String 数据类型')
a='abcde'

print('ab' in a)  # True
print('ad' in a)  # False

print(a)        #abcde
print(a[1:3])   #bc
print(a[0:-1])  #abcd
print(a[0])     #a
print(a[0:])    #abcde
print(a*3)      #abcdeabcdeabcde
print(a+"test") #abcdetest

##反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串
print('abc\nde')
print(r'abc\nde')
del a
print()

#List列表数据类型
print("#List列表数据类型")
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2,True ]
print(list)         #['abcd', 786, 2.23, 'runoob', 70.2, True]
print(list[0])      #abcd
print(list[-1])     #True
print(list[0:])     #['abcd', 786, 2.23, 'runoob', 70.2, True]
print(list[0:-1])   #['abcd', 786, 2.23, 'runoob', 70.2]
print(list*2)       #['abcd', 786, 2.23, 'runoob', 70.2, True, 'abcd', 786, 2.23, 'runoob', 70.2, True]
print(list+list)    #['abcd', 786, 2.23, 'runoob', 70.2, True, 'abcd', 786, 2.23, 'runoob', 70.2, True]

##与Python字符串不一样的是，列表中的元素是可以改变的
list[0:3]=[1,2,3]
print(list)         #[1, 2, 3, 'runoob', 70.2, True]
list[-1]=False
print(list)         #[1, 2, 3, 'runoob', 70.2, False]
del list
print()

#tuple 元组数据类型   元组（tuple）与列表类似，不同之处在于元组的元素不能修改
print('#tuple 元组数据类型')
tuple=( 'abcd', 786 , 2.23, 'runoob', 70.2,True)
print(tuple)         #('abcd', 786, 2.23, 'runoob', 70.2, True)
print(tuple[0])      #abcd
print(tuple[-1])     #True
print(tuple[0:])     #('abcd', 786, 2.23, 'runoob', 70.2, True)
print(tuple[0:-1])   #('abcd', 786, 2.23, 'runoob', 70.2)
print(tuple*2)       #('abcd', 786, 2.23, 'runoob', 70.2, True, 'abcd', 786, 2.23, 'runoob', 70.2, True)
print(tuple+tuple)   #('abcd', 786, 2.23, 'runoob', 70.2, True, 'abcd', 786, 2.23, 'runoob', 70.2, True)

print('a' in tuple)  # False
print('abcd' in tuple)  # True

##字符串看作一种特殊的元组
tup1=()     # 空元组
tup2=(1)    # 不是元组
tup3=(1,)   # 一个元素，需要在元素后添加逗号
print(tup1,tup2,tup3)       #() 1 (1,)
print(type(tup1),type(tup2),type(tup3)) # <class 'tuple'> <class 'int'> <class 'tuple'>

del tuple,tup1,tup2,tup3
print()

# Set 集合数据类型
print("#Set 集合数据类型")
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
if 'Rose' in student:
    print('Rose in student')
else:
    print("Rose not in student")

a = set('abcdef')
b = set('defghi')
print(a,b)  # {'c', 'e', 'a', 'b', 'f', 'd'} {'h', 'g', 'f', 'e', 'd', 'i'}
print(a-b)  # a和b的差集 {'c', 'b', 'a'}
print(a|b)  # a和b的并集 {'h', 'd', 'e', 'c', 'a', 'i', 'b', 'g', 'f'}
print(a&b)  # a和b的交集 {'f', 'e', 'd'}
print(a^b)  # a和b中不同时存在的元素 {'b', 'a', 'i', 'h', 'g', 'c'}

del student,a,b
print()

#Dictionary（字典数据类型） 相当于Map 创建空字典使用 { }
print('#Dictionary（字典数据类型）')
dict = {}
print(type(dict))

dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

del dict,tinydict

print('=========================')
def a():
    '''这是文档字符串'''
    pass
print(a.__doc__)







