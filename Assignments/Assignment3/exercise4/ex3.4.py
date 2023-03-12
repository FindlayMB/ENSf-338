import threading
import random
import time


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        while True:
            self.lock()
            if self.head != (self.tail+1) % self.size:
                if self.head == -1:
                    # if queue is empty head and tail are updated to 0
                    self.head = self.tail = 0
                else:
                    self.tail = (self.tail+1) % self.size
                self.queue[self.tail] = data
                self.unlock()
                return
            self.unlock()
            time.sleep(1)

    def dequeue(self):
        while True:
            self.lock()
            if self.head != -1:
                # Check to see if queue is not empty
                temp = self.queue[self.head]  # return value
                if self.head == self.tail:
                    # if only 1 element in queue
                    self.head = self.tail = -1
                else:
                    self.head = (self.head+1) % 5
                self.unlock()
                return temp
            self.unlock()
            time.sleep(1)


def producer():
    while True:
        number = random.randint(1, 10)
        # random number from [1,10]
        time.sleep(number)
        # thread waits for 1-10 seconds depending on 'number'
        q.enqueue(number)
        # enqueue number into circular queue


def consumer():
    while True:
        number = random.randint(1, 10)
        # random number from [1,10]
        time.sleep(number)
        # thread waits for 1-10 seconds depending on 'number'
        removed = q.dequeue()
        print(f"Element removed: {removed}")


if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
