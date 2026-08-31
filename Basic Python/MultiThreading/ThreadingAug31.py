import threading
import time

# print("the practice on multithreading on Aug 31")


# def download_file(file,seconds):
#     print(f"Dowinloading the {file}")
#     time.sleep(seconds)
#     print(f"Finished downloading {file}")

# thread1 = threading.Thread(target=download_file, args=("movie.mp4",3))
# thread2 = threading.Thread(target=download_file, args=("music.mp3",4))
# thread3 = threading.Thread(target=download_file, args=("book.pdf",2))

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()

# print("All downloads has finished !")

def square(num):
    print(f"the square of {num} is {num * num}")
    time.sleep(1)

th1 = threading.Thread(target=square, args=(10,))
th2 = threading.Thread(target=square, args=(20,))
th3 = threading.Thread(target=square, args=(30,))
th4 = threading.Thread(target=square, args=(40,))
th5 = threading.Thread(target=square, args=(50,))

th1.start()
th2.start()
th3.start()
th4.start()
th5.start()

th1.join()
th2.join()
th3.join()
th4.join()
th5.join()
print("All the calculations has completed !")