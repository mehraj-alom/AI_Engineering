# # # 1. Write a Python program to calculate the sum of a list of numbers using recursion.
# def sum_rec(arr):
#     if len(arr) == 0:
#         return 0
#     if len(arr) == 1:
#         return arr[0]
#     else :
#         return arr[0] + sum_rec(arr[1: ])
def sum_rec(arr):
    if len(arr) == 0:  # Base case: empty list
        return 0
    return arr[0] + sum_rec(arr[1:])




listt = [2]
print(sum_rec(listt))

# # 3. Write a Python program to sum recursion lists using recursion.
# # test_data: [1, 2, [3,4], [5,6]]
# # Expected Result: 21
# def sum (test_data):
#     total = 0
#     if len(test_data) == 0:
#         return 0
#     for element in test_data:
#         if not isinstance(element,list):
#             total += element
#         else:
#              total += sum(element)
#     return total
# test_data= []
# print(sum(test_data))
# test_data = [1, 2, [3,4], [5,6]]
# print(sum(test_data))


# # Write a Python program to solve the Fibonacci sequence using recursion
# def fibo(n):
#     if n == 0 or n == 1:
#         return 1
#     # if n == 1:
#     #     return 1
#     else :
#         return fibo(n-1) + fibo(n-2)
# n = 7
# print("0",end = " ")
# for i in range(n-1):
#     print(fibo(i),end = " ")
# print("\n")
    
# #Write a Python program to get the factorial of a non-negative integer using recursion
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     # if n == 1:
#     #     return 1
#     else :
#         return n * fact(n-1)
    
# n = 5
# for i in range(1,n+1):
#     print(fact(i),end = " ")
# print("\n")

# #  Write a Python program to get the sum of a non-negative integer using recursion.
# # Test Data:
# # sumDigits(345) -> 12
# # sumDigits(45) -> 9

# def sum1(n):
#     if n == 0:
#         return 0
#     else :
#         return n % 10 + sum1(int(n/10))
# print(sum1(345))

# 7. Write a Python program to calculate the sum of the positive integers 
# of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .
# Test Data:
# sum_series(6) -> 12
# sum_series(10) -> 30

def sum2(n):
    if n < 0:
        return 0
    else :
        return n + sum2(n-2) 
print(sum2(10))

