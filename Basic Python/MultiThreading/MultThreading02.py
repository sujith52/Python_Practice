print("thread safety ")
import threading
class ThreadSafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    def increment(self):
        with self.lock:
            self.value += 1
def increment_counter(counter, num_iterations):
    for _ in range(num_iterations):
        counter.increment()

counter = ThreadSafeCounter()
thread1 = threading.Thread(target=increment_counter, args=(counter,100))
thread2 = threading.Thread(target=increment_counter, args=(counter, 200))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f"The final counter value {counter.value}")

import threading
def print_square(num):
    print(f"The square of {num} is {num * num}")
def print_cube(num):
    print(f"The square of {num} is {num * num * num}")
thread1 = threading.Thread(target=print_square, args=(4,))
thread2 = threading.Thread(target=print_cube, args=(6,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

import threading
import time

def work():
    print("working on day")
    time.sleep(2)
    print("working at night !")
thread1 = threading.Thread(target=work)
thread2 = threading.Thread(target=work)
start_time = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end_time = time.time()
print(f"The time taken was {end_time - start_time  }")

import threading
import time

shared_resource = 0
semaphore = threading.Semaphore(2)
def accessing_resourse():
    global shared_resource
    semaphore.acquire()
    print("Thread {} acquired the semaphore.".format(threading.current_thread().name))
    shared_resource += 1
    time.sleep(1)
    print("Thread {} acquired the semaphore.".format(threading.current_thread().name))
    shared_resource -= 1
    semaphore.release()

threads = []
for i in range(5):
    thread = threading.Thread(target=accessing_resourse)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print("all ther threads have completed bro !")

print("thread local class - used to store the instances of thread data locally !")
import threading
thread_local_data = threading.local()
def print_data():
    print("Thread {} has data : {}".format(threading.current_thread().name, thread_local_data.my_data))
def set_thread_data():
    thread_local_data.my_data = "Hello from {}".format(threading.current_thread().name)
    print_data()
thread1 = threading.Thread(target=set_thread_data, name="Sujith")
thread2 = threading.Thread(target=set_thread_data, name="Lathas")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Process has been completed sucessfully !")