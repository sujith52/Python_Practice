# print("Thread pooling")
# from concurrent.futures import ThreadPoolExecutor
# import time 

# def task(message):
#     time.sleep(2)
#     return message

# def main():
#     executor = ThreadPoolExecutor(5)
#     future = executor.submit(task, ("Completed"))
#     print(future.result())
# if __name__ == '__main__':
#     main()

# import threading

# counter = 0
# lock = threading.Lock()

# def increment():
#     global counter
#     with lock:
#         for i in range(5_00):
#             counter += 1
# thread1 = threading.Thread(target=increment)
# thread2 = threading.Thread(target=increment)

# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print(counter)

# import threading
# import queue

# def worker_function(q):
#     try:
#         raise ValueError("there has been an exception in the values !")
#     except Exception as e:
#         q.put(e)
# exception_queue = queue.Queue()
# worker_thread = threading.Thread(target=worker_function, args=(exception_queue,))
# worker_thread.start()
# worker_thread.join()
# while not exception_queue.empty():
#     exception = exception_queue.empty()
#     print(f"A exception occured in the main thread {exception}")
#     break

# import threading
# import queue
# def producer(q):
#     for i in range(5):
#         q.put(i)
#         print(f"produced : {i}")
# def consumer(q):
#     while not q.empty():
#         item = q.get()
#         print(f"Consumed {item}")
# my_queue = queue.Queue()
# producer_thread = threading.Thread(target=producer, args=(my_queue,))
# consumer_thread = threading.Thread(target=consumer, args=(my_queue,))
# producer_thread.start()
# consumer_thread.start()
# producer_thread.join()
# consumer_thread.join()

# print("inter thread communication !")
# import threading
# import queue
# def producer(queue_obj):
#     for i in range(5):
#         queue_obj.put(i)
#         print(f"produced : {i}")
# def consumer(queue_obj):
#     while True:
#         item = queue_obj.get()
#         if item is None:
#             break
#         print(f"Consumer : {item}")
# communication_queue = queue.Queue()
# prod = threading.Thread(target=producer, args=(communication_queue,))
# cons = threading.Thread(target=consumer, args=(communication_queue,))
# prod.start()
# cons.start()
# prod.join()
# cons.join()

print("Thread scheduler !")
import threading
import time
def thread_working(name):
    print(f"{name} has started working")
    time.sleep(4)
    print(f"{name} has stopped working bros !")
th1 = threading.Thread(target=thread_working, args=("Sujith",))
th2 = threading.Thread(target=thread_working, args=("Sreejas",))
th3 = threading.Thread(target=thread_working, args=("Lathas",))
th1.start()
th2.start()
th3.start()
th1.join()
th2.join()
th3.join()