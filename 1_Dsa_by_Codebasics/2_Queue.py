from collections import deque 
import time
import threading
# class queue:
#     def __init__(self):
#         self.container = deque()
#     def push(self,item):
#         self.container.appendleft(item)
#     def pop(self):
#         if  not self.is_empty():
#             self.container.pop()
#         else:
#             raise IndexError("container is emoty ")
#     def is_empty(self):
#         return len(self.container) == 0
#     def size(self):
#         return len(self.container)
#     def print(self):
#         if not self.is_empty():
#             print(list(self.container))
#         else:
#             raise MemoryError("container blank")
# q = queue()
# q.push(19)
# q.push(28)
# q.print()
# q.pop()
# print(q.is_empty())
# q.print()
# q.pop()
# print(q.is_empty())
# q.push(11)
# q.print()

# Data structure tutorial
# exercise: Queue
# For all exercises use Queue class implemented in main tutorial.

# Design a food ordering system where your python program will run two threads,

# Place Order: This thread will be placing an order and inserting that into a queue. 
# This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order 
# out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
# Use this video to get yourself familiar with multithreading in python

# Pass following list as an argument to place order thread,

# orders = ['pizza','samosa','pasta','biryani','burger']



# class queue:
#     def __init__(self):
#         self.container = deque()
#     def order(self,orders):
#         for item in orders:
#             self.container.appendleft(item)
#             print("Order : ",item,end = " ")
#             t = time.time()
#             local_time = time.localtime(t)
#             formatted_time = time.strftime("%H:%M:%S", local_time)
#             print("time:", formatted_time)
#             time.sleep(0.3)
#     def serve(self):
#         if not self.is_empty():
#             a = self.container.pop()
#             print("served : ",a,end = " ")
#             t = time.time()
#             local_time = time.localtime(t)
#             formatted_time = time.strftime("%H:%M:%S", local_time)
#             print("time:", formatted_time)
#             time.sleep(0.4)
#         else:
#             raise LookupError("container is empty")
#     def is_empty(self):
#         return len(self.container) == 0
        
# q = queue()  
# def order(orders,q):
#     q.order(orders)
# def serve(q,set_event):
#     while True:
#         if not q.is_empty():
#             q.serve()
#         elif stop_event.is_set():
#             break
# orders = [
#     'pizza', 'samosa', 'pasta', 'biryani', 'burger', 'momo', 'amul_cool', 'water', 
#     'salad', 'fries', 'chicken_wings', 'hot_dog', 'cheese_burger', 'pasta_bake', 
#     'french_fries', 'pav_bhaji', 'chole_bhature', 'spring_roll', 'dosa', 'idli', 
#     'vada', 'bhel_puri', 'pani_puri', 'aloo_tikki', 'samosa_chat', 'manchurian', 
#     'veg_burger', 'mac_n_cheese', 'noodles', 'fried_rice', 'mushroom_pizza'
# ]

# stop_event = threading.Event()
        
# order_thread = threading.Thread(target=order,args=(orders,q))
# serve_thread = threading.Thread(target=serve,args=(q,stop_event))

# order_thread.start()
# serve_thread.start()
# order_thread.join()
# stop_event.set()
# serve_thread.join()
# time.sleep(9)
# print("All order done and served")



# class queue:
#     def __init__(self):
#         self.container = deque()
#     def order(self,listt):
#         for item in listt:
#             self.container.appendleft(item)
#             print("order :",item)
#             time.sleep(0.2)
#     def serve(self):
#         if not self.is_empty():
#             a = self.container.pop()
#             print("served :",a)
#             time.sleep(0.3)
#         else:
#             raise IndexError("container is empty ")
#     def is_empty(self):
#         return len(self.container) == 0

# def place_order(orders,q):
#     q.order(orders)
# # def serve_order(q):
# #     q.serve()
# def serve_order(q, stop_event):
#     while True:
#         if not q.is_empty():
#             q.serve()
#         elif stop_event.is_set():  # If the stop event is set, exit the loop
#             break
#         else:
#             time.sleep(0.6) 
    
# q = queue()
# orders = [
#     'pizza', 'samosa', 'pasta', 'biryani', 'burger', 'momo', 'amul_cool', 'water', 
#     'salad', 'fries', 'chicken_wings', 'hot_dog', 'cheese_burger', 'pasta_bake', 
#     'french_fries', 'pav_bhaji', 'chole_bhature', 'spring_roll', 'dosa', 'idli', 
#     'vada', 'bhel_puri', 'pani_puri', 'aloo_tikki', 'samosa_chat', 'manchurian', 
#     'veg_burger', 'mac_n_cheese', 'noodles', 'fried_rice', 'mushroom_pizza'
# ]

# stop_event = threading.Event()

# t1 = threading.Thread(target = place_order,args=(orders,q))
# t2 = threading.Thread(target= serve_order, args= (q,stop_event))
# start1 = time.time()
# t1.start()
# t2.start()
# t1.join()
# stop_event.set()
# t2.join()
# print("All orders placed and served!")
# end1 = time.time()

# t = end1 - start1
# print("Time taken = ",t)
    
        
    #     Write a program to print binary numbers from 1 to 10 using Queue. 
    #     Use Queue class implemented in main tutorial. Binary sequence should look like,
    # 1
    # 10
    # 11
    # 100
    # 101
    # 110
    # 111
    # 1000
    # 1001
    # 1010
# class queue:
#     def __init__(self):
#         self.container = deque()
#     def push(self,item):
#         self.container.appendleft(item)
#     def pop(self):
#         return self.container.pop()
#     def is_empty(self):
#         return len(self.container) == 0
# q = queue()
    
# numb = int(input("Enter the number.....: "))
# q.push("1")
# for i in range(numb):
#     bin_num = q.pop()
#     print(bin_num)
#     q.push(bin_num + "0")
#     q.push(bin_num + "1")
#     time.sleep(0.3)
    
    
    
    
     