import threading
import time 

def background_run():
    while True:
        print("The theread is running in background !")
        time.sleep(1)

thread1 = threading.Thread(target=background_run)
thread1.daemon = True
thread1.start()

time.sleep(10)
print("The main even has executed !")

import threading
import time

lock = threading.Lock()
def task(name):
    with lock:
        print(name,"entered")
        print(name,"working on it ")
        print(name,"finished")

th1 = threading.Thread(target=task, args=("Thread1",))
th2 = threading.Thread(target=task, args=("Thread2",))
th1.start()
th2.start()
th1.join()
th2.join()
print("Finished all the threads !")

import threading
import time

lock = threading.Lock()
balance = 1000
def withdraw(amount):
    global balance

    with lock:
        if balance >= amount:
            print(f"Amount withdrawing {amount}")
            balance -= amount
            print(f"The finial balance {balance}")
        else:
            print("somebody get these beggars out of the city")

th1 = threading.Thread(target=withdraw, args=(700,))
th2 = threading.Thread(target=withdraw, args=(100,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f"The main threading was completed !")