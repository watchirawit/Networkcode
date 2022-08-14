from threading import Thread
import threading
import queue
import time

exitFlag = 0

class myThread(Thread):
    def __init__(self, threadID, name, q):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
                       
    def run(self):
        print("Starting " + self.name+"\n")
        self.process_data(self.name,self.q)
        print("Exiting " + self.name + "\n")

    def process_data(self, threadName, q):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                print("%sprocessing%s\n"%(threadName,data))
    
            else:
                queueLock.release()
            time.sleep(1)

threadList = ["Thread-1","Thread-2","Thread-3"]
nameList = ["One","Two","Three","Four","Five"]
queueLock =  threading.Lock()
workQueue =  queue.Queue(10)
threads = []
threadID = 1


for tName in threadList:
   thread = myThread(threadID,tName,workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1
            

queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

while not workQueue.empty():
   pass
#Notify threads it's time to exit
exitFlag = 1
#Wait for all threads to complete
for t in threads:
   t.join()
print("Exiting Main Thread")
            