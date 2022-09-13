import multiprocessing as mp

result = []

def square_list(mylist, result_array, result_value):

    for idx, num in enumerate(mylist):
        result_array[idx] = num*num
    print(f'result (in process): {result_array[:]}')
    result_value.value = sum(result_array)
    print(f'sum of square (in process): {result_value.value}')

if __name__ == "__main__":
    mylist = [1,2,3,4]
    result_array = mp.Array('i',4)
    result_value = mp.Value('i')

    p1 = mp.Process(target=square_list, args=(mylist, result_array, result_value))

    p1.start()
    p1.join()

    print(f'result(in main program): {result_array[:]}')
    print(f'sum of square (in main program): {result_value.value}')