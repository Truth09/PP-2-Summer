# Task-1

def squares(N):
    for i in range(N):
        yield i * i

N = int(input())

for square in squares(N):
    print(square)

# Task-2

def even_nums(n):
    for i in range(0, n+1, 2):
	yield i

n = int(input())

print(",", join(str(num) for num in even_nums(n)))

# Task-3

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())

for i in divisible_by_3_and_4(n):
    print(i)

# Task-4

def squares(a, b):
    for i in range(a, b):
    	yield i * i

a = int(input())
b = int(input())

for i in squares(a, b):
    print(i)

# Task-5

def idk(n):
    for i in range(n, -1,-1):
    	yield i

for i in idk(10):
    print(i)
