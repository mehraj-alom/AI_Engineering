import time
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = 10
print("0 ")
for i in range(n):
    print(fib(i))
    time.sleep(1)