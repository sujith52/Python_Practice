import threading
def print_hello(name):
    print(f"Hello from {name}")

#creating threads 
thread1 = threading.Thread(target=print_hello, args=("Sujith_Thread1",))
thread2 = threading.Thread(target=print_hello, args=("Sreejas_Thread2",))
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("All the threads completed !")

import threading
import time

def count_up_to(max_value):
    count = 1
    while count <= max_value:
        print(f"Count : {count}")
        count += 1
        time.sleep(1)
new_thread = threading.Thread(target=count_up_to, args=(5,))
new_thread.start()
new_thread.join()
print('the threading completed !')

import threading
import time

def cpu_bound_task():
    result = 0
    for i in range(10 ** 7):
        result += i
start_time = time.time()
threads = [threading.Thread(target=cpu_bound_task) for _ in range(2)]
for thread in threads:
    thread.start
for thread in threads:
    thread.join()
print(f"time taken with threads  : {time.time() - start_time}")

import threading
import multiprocessing
import time

def print_nums():
    for i in range(5):
        print(i)
        time.sleep(1)
thred = threading.Thread(target=print_nums)
thred.start()
thred.join()

process = multiprocessing.Process(target=print_nums)
process.start()
process.join()

import threading
def print_nums():
    for i in range(1,6):
        print(f"{threading.current_thread().name} : {i}")

thread1 = threading.Thread(target=print_nums)
thread1.start()

for i in range(6,11):
    print(f"{threading.current_thread().name} : {i}")
thread1.join()

import threading
counter = 0
counter_lock = threading.Lock()

def inc_counter():
    global counter
    with counter_lock:
        counter_value = counter
        counter_value += 1
        counter = counter_value
        print(f"{threading.current_thread().name} : {counter}")
thread1 = threading.Thread(target=inc_counter, name="Thread1")
thread2 = threading.Thread(target=inc_counter, name="Thread2")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('the process has finished !')

import threading
import time 
def background_task():
    while True:
        time.sleep(1)
        print("daemon thread was running in the background !")
daemon_thread = threading.Thread(target=background_task)
daemon_thread.daemon = True
daemon_thread.start()
time.sleep(5)
print("main program ends !")