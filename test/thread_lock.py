import threading
x=0
def increment():
    global x
    x+= 1

def task(lock):
    for _ in range(1000000):
        lock.acquire()
        increment()
        lock.release()

lock = threading.Lock()

t1 = threading.Thread(target=task, args=(lock,))
t2 = threading.Thread(target=task, args=(lock,))

t1.start()
t2.start()

t1.join()
t2.join()

print(x)