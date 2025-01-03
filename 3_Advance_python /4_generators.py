import time
def generator(start = 0):
    while True:
        start += 1
        yield start
gen = generator()
for i in range(100):
    print((next(gen)), end = " ")

def gen2(listt):
    start = 0
    while start < len(listt):
        yield listt[start]
        start += 1
listt = ["my","Name","is","khan",2,4,5,6,8,1]
genn2 = gen2(listt)
for i  in range(len(listt)):
    print(next(genn2))
    time.sleep(0.6)

def generator(data):
    for i in range(len(data)):
        yield data[i]
data = [2,2,3,4,5,6,7,8]
gen = generator(data)
for i in range(len(data)- 1):
    print(next(gen))
print("\n",next(gen))
