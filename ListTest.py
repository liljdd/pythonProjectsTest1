list1 = ['my', 'name', "is", 2000, True];
list2 = [1, 2, 3, 4, 7, 6, 7];

print('list1长度： ',len(list1))
print('list2最大元素：',max(list2))
print('list2最小元素：',min(list2))
# del
del list1[3]
print('删除索引为3的元素：',list1)
# 遍历
for x in list1:
    print(x, end="***")

print('-------------')
list1.append("xxx")
print(list1)
print(list2.count(7))
list1.extend(list2)
print(list1)
list1.pop()
print(list1)
list1.reverse()
print(list1)

aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort()
print(aList)
