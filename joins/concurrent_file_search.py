import os
from os.path import isdir, join
from threading import Lock, Thread


mutex = Lock()
matches = []


def file_search(root, filename):
    print('Searching...', root)
    child_thrads = []
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        # dealing with sub dirs for recursive search
        if isdir(full_path):
            t = Thread(target=file_search, args=([full_path, filename]))
            t.start()
            child_thrads.append(t)
            # file_search(full_path, filename)

        for t in child_thrads:
            t.join()


def main():
    t = Thread(target=file_search, args=(
        ['/Users/vishalborana/Documents/python parallel computing', 'README.md']))
    t.start()
    t.join()

    for m in matches:
        print('Matched: ', m)


main()
