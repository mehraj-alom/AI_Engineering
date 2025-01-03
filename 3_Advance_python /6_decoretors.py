# def dec_func(func):
#     def change():
#         # a = "hello world"
#         # return a
#         print("I am in decoretor")
#         return func()
#     return change

# @dec_func
# def a_func():
#     print(" I am in main function ")
#     return "Original function completed"

# print(a_func())
import time
def dec(fx):
    def mainfx(*args,**kwargs):
        start = time.time()
        result = fx(*args,**kwargs)
        end = time.time()
        print(f"The time taken by {fx.__name__} is {(end - start) }mili sec")
        return result
    return mainfx
        
@dec
def binary_search(arr,low,high,key):
        if low > high:
            return -1
        mid = (low + high) // 2
        if key == arr[mid]:
            return mid 
        elif key < arr[mid]:
            high = mid - 1
            return binary_search(arr,low,high,key)
        else :
            low = mid + 1
            return binary_search(arr,low,high,key)
            
listt = [2]
listt = []
listt = [1,2,3,4,5]
listt = [5,4,3,2,1]
listt = [34,56,89,90,95,100]
length = len(listt) - 1
print("The number is at ", binary_search(listt,0,length,100))












































































































































 
 
 



