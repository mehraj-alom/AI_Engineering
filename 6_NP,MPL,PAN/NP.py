# What is Numpy? 
#what is NUMPY 
#NumPy (Numerical Python) is a powerful library in Python used for numerical and scientific 
# computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection
# of mathematical functions to operate on these arrays. NumPy is a fundamental package for 
# scientific computing and is widely used in data science, machine learning, and engineering applications.
# Why to use Numpy ??
import numpy as np
import time
# a = []
# start = time.time()
# for i in range(10000000):
#     a.append(i)
# end = time.time()
# time1 = start - end 

# start = time.time()
# array = np.arange(10000000, dtype=np.int64)
# end = time.time()
# time2 = start - end 
# print(time1)
# print(time2)

#Using NumPy provides significant advantages over native Python lists for numerical computations,
# especially when working with large datasets. NumPy is faster, as its arrays are stored more 
# efficiently in contiguous memory blocks, allowing for optimized, vectorized operations.
# This reduces overhead compared to Python lists, which require dynamic resizing and introduce 
# additional performance costs during iteration.

# Creation *********
arr = np.array([[10,20,30,40.0],[20,30,39,40],[20,22,28,89]])
print(arr)
print(arr[:2])
print([arr[0]])

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# a
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])
# In NumPy, a dimension of an array is sometimes referred to as an “axis”. This terminology may 
# be useful to disambiguate between the dimensionality of an array and the dimensionality of the
# data represented by the array. For instance, the array a could represent three points, 
# each lying within a four-dimensional space, but a has only two “axes”.

#************Dimension object**************
print(arr.ndim)
print(arr.shape)
print(len(arr.shape) == arr.ndim)
#************** size *********
print(arr.size)
import math
print(arr.size == math.prod(arr.shape))
#Arrays are typically “homogeneous”, meaning that they contain elements of only one
#“data type”. The data type is recorded in the dtype attribute.
print(arr.dtype)

# ======= Important: How to create a basic array =======
# np.zeros
print(np.zeros(6))
# np.ones
print(np.ones(9))
# empty array but why 
# --> he function empty creates an array whose initial content is random and 
#     depends on the state of the memory. The reason to use empty over zeros (or something similar) 
#     is speed - just make sure to fill every element afterwards!
print(np.empty(5))

# np.eye --> This function creates an 2d array (matrix) with diagonals values 1 , it requrires a posiitional argumentt
print(np.eye(4,4)) # np.eye (row,column(optional))

# np.diag --> This function creates a matrix with diagonal as given values and rest as zero 
# it takes two positioanal arguments , 1. array that contain diagonal elements , 2(optional) to shift the 
# diagonal to  a specific range
print(np.diag([2,5,7,9,0,4,5],-1))  # np.diag(diagonal_elemnts , (optioanl) to shift the diagonal )

# array with a range of elements
# --> initialized with a range of elements 
print(np.arange(10))
print(np.arange(2,30,3)) # (first , last , step )
# np.linspace()
# --> to create an array with values that are spaced linearly in a specified interval
print(np.linspace(0,10,7)) # (starting , end , number of elements)
# Specify The type of data 
z = np.ones(5,dtype=np.int64)
print(z)
# Adding, removing, and sorting elements ----------------------->
array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])
# Dimension of the array
print(array_example.ndim) # ------->
# Size of the array (starts counting from 1)
print(array_example.size) # -------->
# Shape of the array
print(array_example.shape)
# To get the diagonal elements 
# --> print(np.diag(array_example)) # Error because it works only with 1D (vector) or 2D (matrix)
print(np.diag(arr))
# To generate Random,Number 
print("HERE IT IS ")
print(np.random.rand(2,3))
# --> np.random.randint(0.1,0.2,50) # Error beacuse randint generate random integer number not works with
# floating numbers 
print(np.random.uniform(0.1,0.2,50)) # (Max , min , Number of value to generate )
print(''.join(np.random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*'),15)))
#                                             #np.random.choice(positioanlargumnet, Number of char to gen)
 


# Can you reshape an array?

a = np.arange(6)
print(a)

b = a.reshape(2,3)
print(b)
         #other ways 
print(np.reshape(a,(3,2),"A"))  #np.reshape(a, shape=(3, 2), order="A")
print(np.reshape(a,(3,2),"C"))
print(np.reshape(a,(3,2),"F"))
