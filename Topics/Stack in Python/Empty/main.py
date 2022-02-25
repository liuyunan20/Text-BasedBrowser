from collections import deque

# please don't change the following line
candy_bag = deque(input().split())

# your code here
n = int(input())
candies = []
for _ in range(n):
    operation = input().split()
    if operation[0] == "PUT":
        candy_bag.append(operation[1])
    elif operation[0] == "TAKE":
        if candy_bag:
            candies.append(candy_bag.pop())
        else:
            candies.append("We are out of candies :(")
    else:
        print("Invalid input")
for candy in candies:
    print(candy)
