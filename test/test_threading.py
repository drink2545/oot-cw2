import threading
from time import sleep
import time
def task1():
    print('start task1')
    sleep(10)
    print('done task1')

def task2():
    print('start task2')
    sleep(5)
    print('done task2')

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
end = time.time()

print(end-start)
print('done both task')