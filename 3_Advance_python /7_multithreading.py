import threading
import time

def calcute_cube(n,stop_event):
    for i in range(n):
        if not stop_event.is_set():
            print("cube of ",i," is " , i**3)
            time.sleep(0.6)
        else:
            break
def calculate_sq(n,stop_event):
    for i in range(n):
        if not stop_event.is_set():
            print("sq of ",i," is " , i**2)
            time.sleep(0.8)
        else :
            break
stop_event = threading.Event()
t1 = threading.Thread(target = calcute_cube,args=(5,stop_event))
t2 = threading.Thread(target = calculate_sq , args=(50,stop_event))
t1.start()
t2.start()
time.sleep(1 )
stop_event.set()
t1.join()
t2.join()
