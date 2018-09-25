from collections import deque

# 将列表当做堆栈使用
stack = [3, 4, 5]
stack.append(6)
print(stack)
stack.pop()
print(stack)

print('=========')
# 将列表当作队列使用
list = [3, 4, 5]
list.append(6)
print(list)
del list[0]  # 效率低
print(list)

queue = deque(list)
print(queue, type(queue))
queue.append(7)
print(queue)
queue.popleft()
print(queue)

print('**************************************')
list1 = [2, 4, 6]
list2 = [3 * x for x in list1]
print(list2)
list3 = [[x, x ** 2] for x in list1]
print(list3)
list4 = [[x, x ** 2] for x in list1 if x > 3]
print(list4)

print('######################################')
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
newfruit = [a.strip() for a in freshfruit]
print(newfruit)

print('-------------------------------------')
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for i in knights.items():
    print(i)    # ('gallahad', 'the pure')

for key, value in knights.items():
    print(key, '=', value)  # gallahad = the pure
