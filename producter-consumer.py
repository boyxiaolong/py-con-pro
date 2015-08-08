from threading import Thread, Lock
import time
import random
import copy
import Queue

queue = []
lock = Lock()
 
class ProducerThread(Thread):
    def run(self):
        nums = range(5) 
        global queue
        while True:
            num = random.choice(nums) 
            lock.acquire()
            queue.append(num)
            lock.release()
            print "Produced", num 
            time.sleep(random.random())
 
class ConsumerThread(Thread):
    def run(self):
        global queue
        tmp_queue = []
        while True:
            lock.acquire()
            if  queue:
                tmp_queue = copy.deepcopy(queue)
                queue = []
            lock.release()
            for data in tmp_queue:
                print "Consumed", data 
            tmp_queue = []
            time.sleep(random.random())
 
ProducerThread().start()
ConsumerThread().start()