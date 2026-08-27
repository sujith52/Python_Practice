print("Multi thereadding in the python")
import threading
import time
def nums():
    print(" 1\n 2\n 3\n 4\n 5")
def chars():
    print(" A \n B \n C \n D \n E")

nums()
chars()

def print_nums():
    for nu in range(1,6):
        print(f"Number : {nu}")
        time.sleep(3)

def print_chars():
    for x in "ABCDE":
        print(f"Characters : {x}")
        time.sleep(3)

t1 = threading.Thread(target=print_nums)
t2 = threading.Thread(target=print_chars)
t1.start()
t2.start()

print_nums()
print_chars()

import threading
import time
def download():
    print("downloading ")
    time.sleep(3)
def music():
    print("playing the music ! ")
    time.sleep(3)
dow = threading.Thread(target=download)
mus = threading.Thread(target=music)
dow.start()
mus.start()
dow.join()
mus.join()

def get_user():
    print("Fetching the users")
    time.sleep(3)
    print("User data fetched! (3s)")
def get_notifications():
    print("Fetching the notifications")
    time.sleep(2)
    print("User nots fetched! (2s)")
def get_recommendations():
    print("Fetching the recomandations")
    time.sleep(4)
    print("User recomendation fetched! (4s)")

start_time = time.time()
t1 = threading.Thread(target=get_user)
t2 = threading.Thread(target=get_notifications)
t3 = threading.Thread(target=get_recommendations)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
end_time = time.time()
print(f"The time taken was {end_time - start_time}")