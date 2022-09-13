import threading
x=0
def increment():
    global x
    x+= 1

def task():
    for _ in range(1000000):
        increment()
if __name__ == '__main__':
    x = 0
    t1 = threading.Thread(target=task)
    t2 = threading.Thread(target=task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

print(x)