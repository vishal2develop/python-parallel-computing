import time
from threading import Thread, Lock

'''
Lock ensure only one thread acceses the code that is locked
'''


class StingySpendy:
    money = 100
    # creating the lock
    mutex = Lock()

    def stingy(self):
        for i in range(1000000):
            # locking the below lines of code
            self.mutex.acquire()
            self.money += 10
            # releasing the lock
            self.mutex.release()
        print("Stingy Done")

    def spendy(self):
        for i in range(1000000):
            # locking the below lines of code
            self.mutex.acquire()
            self.money -= 10
            # releasing the lock
            self.mutex.release()
        print("Spendy Done")


ss = StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
time.sleep(5)
print('Money in the end', ss.money)
