import threading
import time
import random

#threading tutorial.
# time in string format - time.strftime("%Y-%M-%D %H:%M:%S")
def execute_thread():
    print("Thread {} sleeps as {}".format(i,time.strftime("%H:%M:%S", time.gmtime())))

    rand_sleep_time = random.randint(1, 4)
    time.sleep(rand_sleep_time)
    print("Thread {} stops sleeping as {}".format(i,time.strftime("%H:%M:%S", time.gmtime())))

for i in range (10):
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()

    print("Active Threads :", threading.active_count())

    print("Thread Objects: ", threading.enumerate())


