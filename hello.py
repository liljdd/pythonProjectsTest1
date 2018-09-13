i = 10
print(i)
a = " wo shi  shui\n "
b = a.split(" ")
c = a.lstrip()
print(b)
print(c)
print("**".join(b))
d = "你好，世界"
print(d)

del a, b, c
print('###############')
a, b = 0, 1
while b < 100:
    print(b, end=',')
    a, b = b, a + b
