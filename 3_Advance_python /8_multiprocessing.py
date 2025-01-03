import multiprocessing
import time

def calculate_cube(n):
    for i in range(n):
        print("cube of ",i," is " , i**3)
        time.sleep(0.6)
        
def calculate_sq(n):
    for i in range(n):
        print("sq of ",i," is " , i**2)
        time.sleep(2)

p1 = multiprocessing.Process(target=calculate_sq , args=(5,))
p2 = multiprocessing.Process(target=calculate_cube , args=(5,))
p1.start()
p2.start()
p1.join()
p2.join()