import multiprocessing
from multiprocessing.context import Process
import time


def print_array_elements(array):
    while True:
        print(*array, sep=', ')
        time.sleep(1)


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    # normal list will be passed as copy and each process has new list
    # pass by value instead of pass by reference
    arr = [-1]*10
    # to overcome above problem, we can create array from multiprocessing package
    # it is a type of shared memory
    '''
    i = integer type of data
    initialize array with data = [-1]*10
    lock = True (Default)
    '''
    arr = multiprocessing.Array('i', [-1]*10, lock=True)
    p = Process(target=print_array_elements, args=([arr]))
    p.start()
    for j in range(10):
        time.sleep(2)
        for i in range(10):
            arr[i] = j
