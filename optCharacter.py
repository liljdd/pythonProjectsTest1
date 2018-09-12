a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c)

a = 9
b = 5
c = a // b
print("7 - c 的值为：", c)

d = a==b
print(type(d),"===",d)

print()
# Python逻辑运算符  非0为True，True=1 False=0
print("# Python逻辑运算符")
a,b,c,d,e,f,g = 10,20,0,1,-1,True,False
print(a+True,a+False) # 11 10

##	x and y 布尔"与"：如果 x 为 False，x and y 返回 x，否则它返回 y 的计算值
print(c and b)      #0
print(g and b)      #False
print(e and f)      #True
print(e and b)      #20
print('----')

## x or y  v布尔"或"： 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。
print(c or b)      #20
print(g or b)      #20
print(e or b)      #-1
print(f or a)      #True
print(g or a)      #10
print(c or g)      #False
print('-------')

## not x 布尔"非": 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
### a,b,c,d,e,f,g = 10,20,0,1,-1,True,False
print(not a) #False
print(not c) #True
print(not d) #False
print(not e) #False
print(not f) #False
print(not g) #True