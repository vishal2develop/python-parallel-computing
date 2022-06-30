import time
from threading import Thread, Condition


class StingySpendy:
    money = 100
    cv = Condition()

    def stingy(self):
        for i in range(20):
            # locking the below lines of code
            self.cv.acquire()
            self.money += 10
            self.cv.notify()
            # releasing the lock
            self.cv.release()
        print("Stingy Done")

    def spendy(self):
        for i in range(10):
            self.cv.acquire()
            # if there isn't enough money to withdraw,wait
            while self.money < 20:
                print('waiting...')
                self.cv.wait()
            # print('waiting done')
            self.money -= 20
            if self.money < 0:
                print('Money in bank: ', self.money)
            print('releasing...')
            self.cv.release()

        print('Spendy Done')


ss = StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
time.sleep(5)
print('Money in the end: ', ss.money)
