import multiprocessing as mp
from time import sleep
import time
def task1():
    print('start task1')
    x = 0
    for _ in range(100000000):
        x += 1
    print('done task1')

def task2():
    print('start task2')
    x = 0
    for _ in range(100000000):
        x += 1
    print('done task2')

if __name__ == '__main__':

    p1 = mp.Process(target=task1)
    p2 = mp.Process(target=task2)
    start = time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end = time.time()
    print(end-start, 'done')