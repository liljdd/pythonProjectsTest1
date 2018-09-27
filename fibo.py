def area(width, heigth):
    return width * heigth


# 斐波那契(fibonacci)数列模块
def fibo1(a):
    i, j = 0, 1
    print(i, end=" ")
    while (j < a):
        print(j, end=" ")
        j, i = i + j, j
    print()
    return j


def fibo2(n):  # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


fibo1(10)
print(fibo2(10))
fibo2(10)

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')
