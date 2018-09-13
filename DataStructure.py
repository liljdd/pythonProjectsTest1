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
print(queue,type(queue))
queue.append(7)
print(queue)
queue.popleft()
print(queue)
