from threading import Thread

class myThread(Thread):
    def __init__(self,name):
        Thread .__init__(self)
        self.name=name
    def run(self):
       print("Hello,my nam is%s\n"%self.getName())
                         
process1 = myThread("Thread1")
process2 = myThread("Thread2")
process3 = myThread("Thread3")
process1.start()
process2.start()
process3.start()