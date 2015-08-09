from threading import Thread, Condition
import time
import random
import copy

queue = []
con = Condition()
 
class ProducerThread(Thread):
    def run(self):
        nums = range(5) 
        global queue
        is_empty = False
        while True:
            num = random.choice(nums) 
            con.acquire()
            is_empty = len(queue) == 0
            queue.append(num)
            if is_empty:
            	con.notify()
            con.release()
            print "Produced", num 
            time.sleep(random.random())
 
class ConsumerThread(Thread):
    def run(self):
        global queue
        tmp_queue = []
        while True:
            con.acquire()
            if  queue:
                tmp_queue = copy.deepcopy(queue)
                queue = []
            else:
            	con.wait()
            con.release()
            for data in tmp_queue:
                print "Consumed", data
            tmp_queue = []
            
            #time.sleep(random.random())
 
ProducerThread().start()
ConsumerThread().start()