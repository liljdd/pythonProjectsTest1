import os
import sys

# xx
# f = open("c:/Users/Administrator/Desktop/test.txt", "a+")
#
# f.write("zzz")
# f.close()

f = open("c:/Users/Administrator/Desktop/test.txt", "r")
# str = f.read()
# str = f.readline()
# str = f.readlines()
# print(str)

for line in f:
    print(line, end='')

f.close()
print()
print("=======================")
a = os.getcwd()
print(a)

# try:
#     f = open('c:/Users/Administrator/Desktop/test.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError as err:
#     print("Could not convert data to an integer....{0}".format(err))
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

print("===========#########=============")
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
