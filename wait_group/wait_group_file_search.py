import os
from os.path import isdir, join
from threading import Lock, Thread, Condition

mutex = Lock()
matches = []


class WaitGroup:
    wait_count = 0
    cv = Condition()

    def add(self, count):
        self.cv.acquire()
        self.wait_count += 1
        self.cv.release()

    def done(self):
        self.cv.acquire()
        if self.wait_count > 0:
            self.wait_count -= 1
        if self.wait_count == 0:
            self.cv.notify_all()
        self.cv.release()

    def wait(self):
        self.cv.acquire()
        while self.wait_count > 0:
            self.cv.wait()
        self.cv.release()


def file_search(root, filename, wait_group):
    print('Searching...', root)
    # child_thrads = []
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        # dealing with sub dirs for recursive search
        if isdir(full_path):
            # creating child thread and adding to wait_group count
            wait_group.add(1)
            t = Thread(target=file_search, args=(
                [full_path, filename, wait_group]))
            t.start()

    wait_group.done()


def main():
    wait_group = WaitGroup()
    wait_group.add(1)
    t = Thread(target=file_search, args=(
        ['/Users/vishalborana/Documents/python parallel computing', 'README.md', wait_group]))
    t.start()
    # main threads waits for search to finish
    wait_group.wait()

    for m in matches:
        print('Matched: ', m)


main()
