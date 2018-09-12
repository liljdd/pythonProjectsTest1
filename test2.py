str = 'Runoob'

#[ ]  包括左侧，不包括右侧，类似 [ )
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符 Runoo
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符 noo
print(str[2:])  # 输出从第三个开始的后的所有字符 noob
print(str * 2)  # 输出字符串两次 RunoobRunoob
print(str + '你好')  # 连接字符串 Runoob你好

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

#a=input("\n输入：")
#print('a='+a)

#同一行显示多条语句
import  sys;x='xxxxxxx';sys.stdout.write(x+'\n')

print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print ("-->"+i)
print ('\n python 路径为',sys.path)

print("------***--------")

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出 如果要实现不换行需要在变量末尾加上 end=""
print(x, end="= =")
print(y, end="*** ")
print()