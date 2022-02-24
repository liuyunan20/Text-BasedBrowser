from collections import deque


my_stack = deque()
n = int(input())
for _ in range(n):
    operation = input().split()
    if operation[0] == "PUSH":
        my_stack.append(operation[1])
    elif operation[0] == "POP":
        my_stack.pop()
    else:
        print("Invalid input")
for _ in range(len(my_stack)):
    print(my_stack.pop())
